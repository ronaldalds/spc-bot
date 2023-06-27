import os
from pyrogram import Client
from pyrogram.types import Message
from process.relatorio import relatorio
from dotenv import load_dotenv

load_dotenv()

def handle_report(client: Client, message: Message):
    # Verifique se a mensagem contém um comando válido
    relatorio(client, message)


