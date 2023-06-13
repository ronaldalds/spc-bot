import pandas
import os
from process.spc import include
from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
import concurrent.futures
from driver.formatador import formatar_data

load_dotenv()

def handle_include_spc(client: Client, message: Message):
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
            message.reply_text(f"Processando arquivo XLSX com {file.shape[0]}")
            for i in file.iterrows():
                if i[1]['Tipo de Pessoa'] == 'física':
                    # print(formatar_data(str(i[1]['Data Vencimento'])), formatar_data(str(i[1]['Data Compra'])))
                    lista.append((
                        str(i[1]['CPF/CNPJ']),  # cpf_cnpj
                        formatar_data(str(i[1]['Data Nascimento'])),  # data_nascimento
                        str(i[1]['DDD']),  # ddd
                        str(i[1]['Celular']),  # celular
                        str(i[1]['CEP']),  # cep
                        str(i[1]['Logradouro']),  # logradouro
                        str(i[1]['Número']),  # número
                        str(i[1]['Complemento']),  # complemento
                        str(i[1]['Bairro']),  # bairro
                        formatar_data(str(i[1]['Data Vencimento'])),  # data_vencimento
                        formatar_data(str(i[1]['Data Compra'])),  # data_compra
                        str(i[1]['Cod Cliente']),  # cod_cliente
                        str(i[1]['Valor do Débito']).replace('.', ','),  # valor_debito
                    ))

            def executar(arg):
                try:
                    include(
                        cpf_cnpj = arg[0],
                        data_nascimento = arg[1],
                        ddd = arg[2],
                        celular = arg[3],
                        cep = arg[4],
                        logradouro = arg[5],
                        numero = arg[6],
                        complemento = arg[7],
                        bairro = arg[8],
                        data_vencimento = arg[9],
                        data_compra = arg[10],
                        cod_cliente = arg[11],
                        valor_debito = arg[12],
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