from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
from process.faturamento import faturamento
from datetime import datetime, timedelta
import time

load_dotenv()


def handle_start_invoicing(client: Client, message: Message):
    global running
    running = True
    regra = [2,5,8,17,25,27]
    faturamento_processado = False

    while running:
        data_atual = datetime.now()
        data_final = data_atual + timedelta(days=29) 
        data_vencimento = data_atual + timedelta(days=8)

        if data_vencimento.day in regra:
            if not faturamento_processado:
                faturamento(
                    regra = f"Dia {data_vencimento.day:02}",
                    data_inicial = datetime.strftime(data_atual, "%d%m%Y"),
                    data_final = datetime.strftime(data_final, "%d%m%Y"),
                    data_vecimento = datetime.strftime(data_vencimento, "%d%m%Y")
                    )
                faturamento_processado = True

        if faturamento_processado and (data_vencimento.day not in regra):
            faturamento_processado = False




        # Aguarda antes de verificar novamente valor em segundos
        time.sleep(5 * 1 * 1) # segundos * minutos * horas

        # Verifica se a execução deve continuar ou parar
        if not running:
            message.reply_text("Faturamento parado")
            break

def handle_stop_invoicing(client: Client, message: Message):
    global running
    running = False
    message.reply_text("Pedido de parada iniciado...")
    

def handle_status_invoicing(client: Client, message: Message):
    global running
    try:
        if running:
            message.reply_text("Faturamento em execução")
        else:
            message.reply_text("Faturamento parado")
    except:
        message.reply_text("Faturamento parado")
