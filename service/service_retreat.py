import openpyxl
import os
import time
from process.recolhimento import recolhimento
from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
import concurrent.futures
from driver.formatador import formatar_int, formatar_documento

load_dotenv()

running = False

def handle_start_retreat_mk(client: Client, message: Message):
    global running
    if not running:
        running = True
        # Verifique se a mensagem contém um documento e se o tipo MIME do documento é "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        if message.document and message.document.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            # Quantidade de itens na Pool
            limite_threads = 20

            # Baixe o arquivo XLSX
            file_path = message.download()
            message.reply_text("Preparando arquivo XLSX")
            
            # Processar o arquivo XLSX conforme necessário
            try:
                try:
                    workbook = openpyxl.load_workbook(file_path)
                except openpyxl.utils.exceptions.InvalidFileException:
                    message.reply_text("O arquivo fornecido não é um arquivo XLSX válido.")
                    return

                sheet = workbook.active
                max_row = sheet.max_row
                lista = []
                headers = [cell.value for cell in sheet[1]]
                for row in sheet.iter_rows(min_row=2, max_row=max_row, values_only=True):
                    if (str(row[headers.index("Qtd Conexoes")]) == "1") and (row[headers.index("OS Cancelamento ou Recolhimento")] == "N"):
                        try:
                            mk = formatar_int(row[headers.index("MK")])
                            contrato = formatar_int(row[headers.index("Contrato")])
                            conexao_associada = formatar_int(row[headers.index("Conexao Associada")])
                            cpf = formatar_documento(row[headers.index("Documento/Codigo")])['cpf']
                            cod = formatar_documento(row[headers.index("Documento/Codigo")])['cod']
                            tipo_da_os = row[headers.index("Tipo OS")]
                            grupo_atendimento_os = str(row[headers.index("Grupo Atendimento OS")]).strip()
                            detalhe_os = row[headers.index("Detalhe OS")]

                            # Se chegou até aqui, os dados são válidos, então adiciona à lista
                            lista.append((
                                mk,
                                contrato,
                                conexao_associada,
                                cpf,
                                cod,
                                tipo_da_os,
                                grupo_atendimento_os,
                                detalhe_os,
                                ))
                        except Exception as e:
                            print(f"Error: na linha {len(lista) + 1}, {e}")

                message.reply_text(f"Processando arquivo XLSX com {len(lista)} contratos...")
                def executar(arg):
                    if running:
                        try:
                            recolhimento(
                                mk=arg[0],
                                contrato=arg[1],
                                conexao_associada=arg[2],
                                cpf=arg[3],
                                cod=arg[4],
                                tipo_da_os=arg[5],
                                grupo_atendimento_os=arg[6],
                                detalhe_os=arg[7]
                            )
                        except Exception as e:
                            print(f"Error executing na função executar:mk:{arg[0]} contrato:{arg[1]} conexão:{arg[2]} {e}")
                    else:
                        message.reply_text(f"Recolhimento mk:{arg[0]} contrato:{arg[1]} conexão:{arg[2]} parado.")

                # Criando Pool
                with concurrent.futures.ThreadPoolExecutor(max_workers=limite_threads) as executor:
                    executor.map(executar, lista)
            # ...
            finally:
            # Excluir o arquivo XLSX
                time.sleep(1)
                os.remove(file_path)
            # Responder à mensagem do usuário com o resultado do processamento do arquivo
            message.reply_text("O arquivo XLSX foi processado com sucesso!")
            running = False
        else:
            # Responder à mensagem do usuário com uma mensagem de erro
            message.reply_text("Por favor, envie um arquivo XLSX para processar.")
    else:
        message.reply_text("Recolhimento em execução.")
    
def handle_stop_retreat_mk(client: Client, message: Message):
    global running
    running = False
    message.reply_text("Pedido de parada iniciado...")

def handle_status_retreat_mk(client: Client, message: Message):
    global running
    try:
        if running:
            message.reply_text("Recolhimento em execução")
        else:
            message.reply_text("Recolhimento parado")
    except:
        message.reply_text("Recolhimento parado")