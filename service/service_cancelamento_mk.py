import pandas
import os
from process.cancelamento import cancelamento
from pyrogram.types import Message
import concurrent.futures
from dotenv import load_dotenv
from driver.formatador import formatar_data, formatar_incidencia, formatar_valor_multa, formatar_int

load_dotenv()

def handle_cancelamento_mk(client, message: Message):
    if str(message.from_user.id) == str(os.getenv("CHAT_ID_FINANCEIRO")):
        # Verifique se a mensagem contém um documento e se o tipo MIME do documento é "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        if message.document and message.document.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            # Criando Pool
            limite_threads = 4

            # Baixe o arquivo XLSX
            message.reply_text("Preparando arquivo XLSX")
            file_path = message.download()
            
            # Processar o arquivo XLSX conforme necessário
            try:
                file = pandas.read_excel(file_path)

                lista = []
                for i in file.iterrows():
                    try:
                        lista.append((
                            formatar_int(i[1]['MK']), # mk
                            formatar_int(i[1]['Cod Pessoa']), # Cod Pessoa
                            formatar_int(i[1]['Contrato']), # Contrato
                            i[1]['Detalhes Cancelamento'], # Detalhes Cancelamento
                            i[1]['Tipo OS'], # Tipo OS
                            i[1]['Grupo Atendimento OS'], # Grupo Atendimento OS
                            i[1]['Relato do problema'], # Relato do problema
                            formatar_incidencia(i[1]['Incidencia de Multa']), # Incidencia de Multa
                            formatar_valor_multa(i[1]['Valor Multa']), # Valor Multa
                            formatar_data(i[1]['Data Vcto Multa Contratual']), # Data Vcto Multa Contratual
                            i[1]['Planos de Contas'] # Planos de Contas
                        ))
                    except:
                        print(f"Error: na linha {i[0] + 2}")

                message.reply_text(f"Processando arquivo XLSX com {len(lista)} contratos")
                # for c,i in enumerate(lista):
                #     print(c+2,i[0],i[1],i[2],i[3][0:10],i[4],i[5],i[6][0:10],i[7],i[8],i[9],i[10])
                def executar(arg):
                    try:
                        cancelamento(
                            mk = arg[0],
                            cod_pessoa = arg[1],
                            contrato = arg[2],
                            detalhes_cancelamento = arg[3],
                            tipo_da_os = arg[4],
                            grupo_atendimento_os = arg[5],
                            relato_do_problema = arg[6],
                            incidencia_multa = arg[7],
                            valor_multa = arg[8],
                            vencimento_multa = arg[9],
                            planos_contas = arg[10]
                        )
                    except Exception as e:
                        print(f"Error executing na função executar: {e}")
                with concurrent.futures.ThreadPoolExecutor(max_workers=limite_threads) as executor:
                    resultados = executor.map(executar, lista)
            # ...
            finally:
            # Excluir o arquivo XLSX
                os.remove(file_path)
            # Responder à mensagem do usuário com o resultado do processamento do arquivo
            message.reply_text("O arquivo XLSX foi processado com sucesso!")
        else:
            # Responder à mensagem do usuário com uma mensagem de erro
            message.reply_text("Por favor, envie um arquivo XLSX para processar.")
    else:
        message.reply_text("command indisponível no momento.")