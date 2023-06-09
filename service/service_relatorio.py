from pyrogram import Client
from pyrogram.types import Message
from process.relatorio import relatorio_cancelamento


def handle_relatorio(client: Client, message: Message):
    # Verifique se a mensagem contém um comando válido
    relatorio_cancelamento(client, message)
