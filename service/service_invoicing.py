from dotenv import load_dotenv
import os
from pyrogram.types import Message
from pyrogram import Client
from process.faturamento import faturamento
from datetime import datetime, timedelta
import time

load_dotenv()

running_mk1 = False
running_mk3 = False
regra = [2,5,8,17,25,27]
tempo_ciclo = int(os.getenv('TIME_CLICO_FATURAMENTO'))

def handle_start_invoicing_mk1(client: Client, message: Message):
    global running_mk1
    if not running_mk1:
        running_mk1 = True
        faturamento_processado_mk1 = False
        message.reply_text("Faturamento mk1 em execução.")

        while running_mk1:
            data_atual = datetime.now()
            data_final = data_atual + timedelta(days=29) 
            data_vencimento = data_atual + timedelta(days=8)

            # saber se o vencimento esta dentro das regras de vencimento
            if data_vencimento.day in regra:
                if not faturamento_processado_mk1:
                    faturamento_processado_mk1 = faturamento(
                        mk = 1,
                        regra = f"Dia {data_vencimento.day:02}",
                        data_inicial = datetime.strftime(data_atual, "%d%m%Y"),
                        data_final = datetime.strftime(data_final, "%d%m%Y"),
                        data_vecimento = datetime.strftime(data_vencimento, "%d%m%Y")
                        )

            # Reseta o valor da variavel de processo
            if faturamento_processado_mk1 and (data_vencimento.day not in regra):
                faturamento_processado_mk1 = False

            # Aguarda antes de verificar novamente valor em segundos
            time.sleep(tempo_ciclo)

            # Verifica se a execução deve continuar ou parar
            if not running_mk1:
                message.reply_text("Faturamento mk1 parado.")
                break
    else:
        message.reply_text("Faturamento mk1 em execução.")

def handle_stop_invoicing_mk1(client: Client, message: Message):
    global running_mk1
    running_mk1 = False
    message.reply_text("Pedido de parada mk1 iniciado...")
    
def handle_status_invoicing_mk1(client: Client, message: Message):
    global running_mk1
    try:
        if running_mk1:
            message.reply_text("Faturamento mk1 em execução")
        else:
            message.reply_text("Faturamento mk1 parado")
    except:
        message.reply_text("Faturamento mk1 parado")

def handle_start_invoicing_mk3(client: Client, message: Message):
    global running_mk3
    if not running_mk3:
        running_mk3 = True
        faturamento_processado_mk3 = False
        message.reply_text("Faturamento mk3 em execução")

        while running_mk3:
            data_atual = datetime.now()
            data_final = data_atual + timedelta(days=29) 
            data_vencimento = data_atual + timedelta(days=8)

            if data_vencimento.day in regra:
                if not faturamento_processado_mk3:
                    faturamento_processado_mk3 = faturamento(
                        mk = 3,
                        regra = f"Dia {data_vencimento.day:02}",
                        data_inicial = datetime.strftime(data_atual, "%d%m%Y"),
                        data_final = datetime.strftime(data_final, "%d%m%Y"),
                        data_vecimento = datetime.strftime(data_vencimento, "%d%m%Y")
                        )

            # Reseta o valor da variavel de processo
            if faturamento_processado_mk3 and (data_vencimento.day not in regra):
                faturamento_processado_mk3 = False

            # Aguarda antes de verificar novamente valor em segundos
            time.sleep(tempo_ciclo * 10)

            # Verifica se a execução deve continuar ou parar
            if not running_mk3:
                message.reply_text("Faturamento mk3 parado.")
                break
    else:
        message.reply_text("Faturamento mk3 em execução.")

def handle_stop_invoicing_mk3(client: Client, message: Message):
    global running_mk3
    running_mk3 = False
    message.reply_text("Pedido de parada mk3 iniciado...")
    
def handle_status_invoicing_mk3(client: Client, message: Message):
    global running_mk3
    try:
        if running_mk3:
            message.reply_text("Faturamento mk3 em execução")
        else:
            message.reply_text("Faturamento mk3 parado")
    except:
        message.reply_text("Faturamento mk3 parado")
