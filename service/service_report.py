import os
from pyrogram import Client
from pyrogram.types import Message
from process.relatorio import relatorio
from dotenv import load_dotenv

load_dotenv()

def handle_report_cancellation(client: Client, message: Message):
    # Verifique se a mensagem contém um comando válido
    relatorio(client, message, process='cancelamento')

def handle_report_spc(client: Client, message: Message):
    # Verifique se a mensagem contém um comando válido
    relatorio(client, message, process='spc')

def handle_report_invoicing(client: Client, message: Message):
    # Verifique se a mensagem contém um comando válido
    relatorio(client, message, process='faturamento')

def handle_report_retreat(client: Client, message: Message):
    # Verifique se a mensagem contém um comando válido
    relatorio(client, message, process='recolhimento')

