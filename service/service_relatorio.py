import os
from pyrogram import Client
from pyrogram.types import Message
from process.relatorio import relatorio
from dotenv import load_dotenv

load_dotenv()

def handle_relatorio_cancelamento(client: Client, message: Message):
    if str(message.chat.id) == str(os.getenv("CHAT_ID_CANCELAMENTO")):
        # Verifique se a mensagem contém um comando válido
        relatorio(client, message, process='cancelamento')
    else:
        message.reply_text("Você não está autorizado a usar este comando.")

def handle_relatorio_spc(client: Client, message: Message):
    if str(message.chat.id) == str(os.getenv("CHAT_ID_SPC")):
        # Verifique se a mensagem contém um comando válido
        relatorio(client, message, process='spc')
    else:
        message.reply_text("Você não está autorizado a usar este comando.")
