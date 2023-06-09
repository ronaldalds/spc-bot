from pyrogram import Client
from pyrogram.types import Message
import datetime
import os


def relatorio_cancelamento(client: Client, message: Message):
    # Extraia a data do comando
    comando, data = message.text.split(' ', 1)
    # Verifique se a data é válida
    try:
        data = datetime.datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        # Data inválida, envie uma resposta de erro
        client.send_message(message.chat.id, "Por favor, envie uma data válida no formato dd/mm/yyyy.")
        return

    data = message.text.split(' ')[1].replace('/', '_')
    # Localize os arquivos no diretório
    diretorio_atual = os.path.dirname(os.path.abspath(__file__)) # Substitua pelo caminho correto para o diretório
    diretorio_logs = os.path.join(diretorio_atual, 'logs')
    arquivos = os.listdir(diretorio_logs)

    # Procure o arquivo correspondente à data
    arquivo_encontrado = None
    for arquivo in arquivos:
        if f'cancelamento_{data}' in arquivo:  # Substitua pelo formato correto do nome do arquivo
            arquivo_encontrado = arquivo
            break

    if arquivo_encontrado:
        # Envie o arquivo
        caminho_arquivo = os.path.join(diretorio_logs, arquivo_encontrado)
        with open(caminho_arquivo, 'rb') as file:
            client.send_document(message.chat.id, file, caption=arquivo_encontrado)
    else:
        # Arquivo não encontrado, envie uma resposta de erro
        client.send_message(message.chat.id, f"Arquivo não encontrado para a data {data.strftime('%d/%m/%Y')}.")
