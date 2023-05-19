from pyrogram import Client
import os
from pyrogram.types import Message

app = Client("my_bot")

@app.on_message(command="processar_xlsx")
def handle_processar_xlsx_command(client, message: Message):
    # Verifique se a mensagem contém um documento e se o tipo MIME do documento é "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    if message.document and message.document.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        # Baixe o arquivo XLSX
        file_path = message.download()
        # Processar o arquivo XLSX conforme necessário
        # ...
        # Excluir o arquivo XLSX
        os.remove(file_path)
        # Responder à mensagem do usuário com o resultado do processamento do arquivo
        message.reply_text("O arquivo XLSX foi processado com sucesso!")
    else:
        # Responder à mensagem do usuário com uma mensagem de erro
        message.reply_text("Por favor, envie um arquivo XLSX para processar.")

app.run()