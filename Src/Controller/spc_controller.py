import os
import concurrent.futures
import pandas as pd
from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
from datetime import datetime
from Src.Service.spc_service import include
from Src.Util.formatador  import formatar_data, formatar_valor_multa

load_dotenv()

running = False

def handle_start_include_spc(client: Client, message: Message):
    global running
    if not running:
        # Verifique se a mensagem contém um documento e se o tipo MIME do documento é "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        if message.document and message.document.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            running = True
            # Criando Pool
            limite_threads = 1

            # Baixe o arquivo XLSX
            file_path = message.download(in_memory=True)
            hora = datetime.now()
            file_name = hora.strftime("%S_%M_%H %Y-%m-%d.log")
            message.reply_text("Preparando arquivo XLSX")
            agente = f"{message.from_user.first_name}.{message.from_user.last_name}"

            # caminho pasta de logs
            diretorio_logs = os.path.join(os.path.dirname(__file__), 'logs')

            # caminho pasta de docs
            diretorio_docs = os.path.join(os.path.dirname(__file__), 'docs')

            # cria pasta de logs em caso de nao existir
            if not os.path.exists(diretorio_logs):
                os.makedirs(diretorio_logs)

            # cria pasta de docs em caso de nao existir
            if not os.path.exists(diretorio_docs):
                os.makedirs(diretorio_docs)
            
            resultados = []
            try:
                try:
                    # Ler o arquivo XLSX usando pandas e especificar a codificação UTF-8
                    df = pd.read_excel(file_path, engine='openpyxl')

                    # Converter o dataframe para uma lista de dicionários
                    lista = df.to_dict(orient='records')

                    # Verificar se a chave 'MK' contém valor NaN
                    lista = [dados for dados in lista if not pd.isna(dados.get('CPF/CNPJ'))]
                    # print(lista)

                    # Criar aquivo de log com todos os contratos enviados para cancelamento
                    with open(os.path.join(diretorio_docs, file_name), "a") as pedido:
                        for c,arg in enumerate(lista):
                            pedido.write(f"{(c + 1):03};SPC;CPF/CNPJ:{arg.get('CPF/CNPJ')};Consumidor:{arg.get('Nome Consumidor')};Débito:{arg.get('Valor do Débito')};Agente:{agente}\n")
                    
                    # Envia arquivo de docs com todos as solicitações de cancelamento
                    with open(os.path.join(diretorio_docs, file_name), "rb") as enviar_docs:
                        client.send_document(os.getenv("CHAT_ID_ADM"),enviar_docs, caption=f"solicitações {file_name}", file_name=f"solicitações {file_name}")

                    
                    message.reply_text(f"Processando arquivo XLSX do SPC com {len(lista)}...")

                except pd.errors.ParserError:
                    message.reply_text("O arquivo fornecido não é um arquivo XLSX válido.")
                    running = False
                    return
                
                def executar(arg: dict):
                    if running:
                        try:
                            cpf_cnpj: str = str(arg.get("CPF/CNPJ"))
                            data_nascimento = formatar_data(arg.get("Data Nascimento"))
                            ddd: str = str(arg.get("DDD"))
                            celular: str = str(arg.get("Celular"))
                            cep: str = str(arg.get("CEP"))
                            logradouro = arg.get("Logradouro")
                            numero = arg.get("Número")
                            complemento = arg.get("Complemento")
                            bairro = arg.get("Bairro")
                            data_vencimento = formatar_data(arg.get("Data Vencimento"))
                            data_compra = formatar_data(arg.get("Data Compra"))
                            cod_cliente: str = str(arg.get("Cod Cliente"))
                            valor_debito = formatar_valor_multa(arg.get("Valor do Débito"))

                            return include(
                                cpf_cnpj = ''.join(caractere for caractere in cpf_cnpj if caractere.isnumeric()),
                                data_nascimento = data_nascimento,
                                ddd = ''.join(caractere for caractere in ddd if caractere.isnumeric()),
                                celular = ''.join(caractere for caractere in celular if caractere.isnumeric()),
                                cep = ''.join(caractere for caractere in cep if caractere.isnumeric()),
                                logradouro = logradouro,
                                numero = numero,
                                complemento = complemento,
                                bairro = bairro,
                                data_vencimento = data_vencimento,
                                data_compra = data_compra,
                                cod_cliente = ''.join(caractere for caractere in cod_cliente if caractere.isnumeric()),
                                valor_debito = valor_debito,
                                )
                        except Exception as e:
                            print(f"Error executar na função include: CPF/CNPJ:{arg.get('CPF/CNPJ')} Consumidor:{arg.get('Nome Consumidor')} Débito:{arg.get('Valor do Débito')} {e}")
                    else:
                        message.reply_text(f"SPC CPF/CNPJ:{arg.get('CPF/CNPJ')};Consumidor:{arg.get('Nome Consumidor')};Débito:{arg.get('Valor do Débito')} parado.")

                # Criando Pool
                with concurrent.futures.ThreadPoolExecutor(max_workers=limite_threads) as executor:
                    resultados = executor.map(executar, lista)
            
            except Exception as e:
                print(f"Ocorreu um erro ao processar o arquivo XLSX: {e}")
                running = False
                return
            
            finally:
                # Criar aquivo de log com todos os resultados de cancelamento
                with open(os.path.join(diretorio_logs, file_name), "a") as file:
                    if resultados:
                        for resultado in resultados:
                            file.write(f"{resultado}\n")

                # Envia arquivo de log com todos os resultados de cancelamento
                with open(os.path.join(diretorio_logs, file_name), "rb") as enviar_logs:
                    message.reply_document(enviar_logs, caption=file_name, file_name=file_name)
                    client.send_document(os.getenv("CHAT_ID_ADM"), enviar_logs, caption=f"resultado {file_name}", file_name=f"resultado {file_name}")

                print("Processo SPC concluído.")
                message.reply_text("O arquivo XLSX de SPC foi processado com sucesso!")
                running = False
                return
        
        else:
            # Responder à mensagem do usuário com uma mensagem de erro
            message.reply_text("Por favor, envie um arquivo XLSX para processar.")
            return
    else:
        message.reply_text("SPC em execução.")

def handle_stop_include_spc(client: Client, message: Message):
    global running
    if running:
        running = False
        message.reply_text("Pedido de parada iniciado...")
        return
    else:
        message.reply_text("SPC parado")
        return
        
def handle_status_include_spc(client: Client, message: Message):
    global running
    try:
        if running:
            message.reply_text("SPC em execução")
            return
        else:
            message.reply_text("SPC parado")
            return
    except:
        message.reply_text("SPC parado")
        return