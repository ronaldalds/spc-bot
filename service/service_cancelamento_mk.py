import pandas
import os
from process.cancelamento import cancelamento
from pyrogram.types import Message
import concurrent.futures
from dotenv import load_dotenv
from driver.formatador import formatar_data

load_dotenv()

def handle_cancelamento_mk01(client, message: Message):
    if str(message.from_user.id) == str(os.getenv("CHAT_ID_SPC")):
        # Verifique se a mensagem contém um documento e se o tipo MIME do documento é "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        if message.document and message.document.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            # Criando Pool
            limite_threads = 20
            # Baixe o arquivo XLSX
            message.reply_text("Preparando arquivo XLSX")
            file_path = message.download()
            # Processar o arquivo XLSX conforme necessário
            try:
                file = pandas.read_excel(file_path)

                lista = []
                message.reply_text(f"Processando arquivo XLSX com {file.shape[0]}")
                for i in file.iterrows():
                    # print(formatar_data(str(i[1]['Data Vencimento'])), formatar_data(str(i[1]['Data Compra'])))
                    lista.append((
                        str(i[1]['mk']).strip(),  # mk
                        str(i[1]['Cod Pessoa']),  # Cod Pessoa
                        str(i[1]['Contrato']),  # Contrato
                        str(i[1]['Detalhes Cancelamento']),  # Detalhes Cancelamento
                        str(i[1]['Tipo OS']),  # Tipo OS
                        str(i[1]['Grupo Atendimento OS']),  # Grupo Atendimento OS
                        str(i[1]['Relato do problema']),  # Relato do problema

                        # dados para multa
                        str(i[1]['Incidencia de Multa']),  # Incidencia de Multa
                        str(i[1]['Valor Multa']),  # Valor Multa
                        str(i[1]['Data Vcto Multa Contratual']),  # Data Vcto Multa Contratual
                        str(i[1]['Planos de Contas']),  # Planos de Contas
                    ))

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

                            # dados para multa
                            incidencia_multa = arg[7],
                            valor_multa = arg[8],
                            vencimento_multa = arg[9],
                            planos_contas = arg[10]
                        )
                    except Exception as e:
                        print(f"Error executing: {e}")
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