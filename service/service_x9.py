from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram import Client
from process.x9 import x9
from datetime import datetime
import time
import os
from queue import Queue
import schedule
import threading

load_dotenv()

resultado_x9 = Queue()
running = False
tempo_ciclo = int(os.getenv('TIME_CLICO_X9'))
grupo_transport = int(os.getenv('CHAT_ID_GROUP_TRANSPORT'))

def chamada():
    global running
    res = x9(datetime.now())
    print(res, type(res))
    if running and res:
        resultado_x9.put(res)

def agendar_funcao():
    print(f"iniciando verificação: {datetime.now()}")
    threading.Thread(target=chamada).start()

def handle_start_x9_mk1(client: Client, message: Message):
    global running
    if not running:
        running = True
        message.reply_text("X9 em execução.")
        job_x9 = schedule.every(tempo_ciclo).minutes.do(agendar_funcao)
        print(f"X9 em execução: {datetime.now()}")

        while running:
            schedule.run_pending()
            time.sleep(10)
            # verifica se existe ocorrência
            if not resultado_x9.empty():
                ocorrencias = resultado_x9.get()
                print(ocorrencia)
                for ocorrencia in ocorrencias:
                    # enviar ocorrências
                    client.send_message(grupo_transport, ocorrencia)

            # Verifica se a execução deve continuar ou parar
            if not running:
                # limpa a fila de resultados
                while not resultado_x9.empty():
                    resultado_x9.get()
                
                schedule.cancel_job(job_x9)
                message.reply_text("X9 parado.")
                break
    else:
        message.reply_text("X9 em execução.")

def handle_stop_x9_mk1(client: Client, message: Message):
    global running
    running = False
    message.reply_text("Pedido de parada do X9 iniciado...")
    
def handle_status_x9_mk1(client: Client, message: Message):
    global running
    try:
        if running:
            message.reply_text("X9 em execução")
        else:
            message.reply_text("X9 parado")
    except:
        message.reply_text("X9 parado")