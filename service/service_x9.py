from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
from process.x9 import x9
from datetime import datetime, timedelta
import time

load_dotenv()

running = False
tempo_ciclo = 60 * 30 * 1 # segundos * minutos * horas

def handle_start_x9_mk1(client: Client, message: Message):
    global running
    if not running:
        running = True
        message.reply_text("X9 em execução.")

        while running:

            # saber se o vencimento esta dentro das regras de vencimento
            x9()

            # Aguarda antes de verificar novamente valor em segundos
            time.sleep(tempo_ciclo)

            # Verifica se a execução deve continuar ou parar
            if not running:
                message.reply_text("X9 parado.")
                break
    else:
        message.reply_text("X9 em execução.")

def handle_stop_x9_mk1(client: Client, message: Message):
    global running
    running = False
    message.reply_text("Pedido do X9 iniciado...")
    
def handle_status_x9_mk1(client: Client, message: Message):
    global running
    try:
        if running:
            message.reply_text("X9 em execução")
        else:
            message.reply_text("X9 parado")
    except:
        message.reply_text("X9 parado")