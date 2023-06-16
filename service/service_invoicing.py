from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
from process.faturamento import faturamento
import datetime
import time

load_dotenv()



def handle_start_invoicing(client: Client, message: Message):
    global running
    running = True

    while running:

        # processo faturamento
        # faturamento()

        # Aguarda antes de verificar novamente valor em segundos
        time.sleep(5 * 1 * 1) # segundos * minutos * horas

        print('continuar rodando')

        # Verifica se a execução deve continuar ou parar
        if not running:
            client.send_message(message.chat.id, f"Faturamento parado")
            break

def handle_stop_invoicing(client: Client, message: Message):
    global running
    running = False
    

def handle_status_invoicing(client: Client, message: Message):
    global running
    try:
        if running:
            client.send_message(message.chat.id, f"Faturamento em execução")
        else:
            client.send_message(message.chat.id, f"Faturamento parado")
    except:
        client.send_message(message.chat.id, f"Faturamento parado")
