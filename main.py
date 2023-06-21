from pyrogram import Client, filters
import os
from pyrogram.types import Message
from dotenv import load_dotenv
from service.service_spc import handle_start_include_spc, handle_stop_include_spc, handle_status_include_spc
from service.service_cancellation import handle_start_cancellation_mk, handle_stop_cancellation_mk, handle_status_cancellation_mk
from service.service_retreat import handle_start_retreat_mk, handle_stop_retreat_mk, handle_status_retreat_mk
from service.service_report import handle_report_cancellation, handle_report_spc, handle_report_invoicing, handle_report_retreat
from service.service_invoicing import (
    handle_start_invoicing_mk1,
    handle_stop_invoicing_mk1,
    handle_status_invoicing_mk1,
    handle_start_invoicing_mk3,
    handle_stop_invoicing_mk3,
    handle_status_invoicing_mk3
    )

load_dotenv()

version = "0.0.3"

app = Client(
    name=os.getenv("BOT_NAME_TELEGRAM"), 
    api_hash=os.getenv("API_HASH_TELEGRAM"),
    api_id=os.getenv("API_ID_TELEGRAM"),
    bot_token=os.getenv("BOT_TOKEN_TELEGRAM")
    )

chat_mis = [
    os.getenv("CHAT_ID_ADM"),
    os.getenv("CHAT_ID_GESTOR_MIS"),
    os.getenv("CHAT_ID_SPC"),
    os.getenv("CHAT_ID_CANCELAMENTO"),
    os.getenv("CHAT_ID_RECOLHIMENTO"),
    ]

chat_ost = [
    os.getenv("CHAT_ID_ADM"),
    ]

chat_financeiro = [
    os.getenv("CHAT_ID_ADM"),
    os.getenv("CHAT_ID_ADM_MK"),
    ]

# Verificação de autorização
def authorization(ids_autorizados):
    def decorador(func):
        def verificacao(client, message: Message):
            if str(message.chat.id) in ids_autorizados:
                return func(client, message)
            else:
                message.reply_text("Você não está autorizado a usar este bot.")
        return verificacao
    return decorador


@app.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text(f"""
/mis - Setor MIS
/ost - Setor OST
/financeiro - Setor Financeiro
/chat - Para informa seu chat_id
""")

@app.on_message(filters.command("ost"))
@authorization(chat_ost)
def ost(client, message: Message):
    message.reply_text(f"""
/verificar - Verifica O.S
""")

@app.on_message(filters.command("mis"))
@authorization(chat_mis)
def mis(client, message: Message):
    message.reply_text(f"""
/spc - Inclui clientes no sistema do spc
/cancelamento - Cancelamento de cliente mk
/recolhimento - O.S de Recolhimento mk
""")
    
@app.on_message(filters.command("financeiro"))
@authorization(chat_financeiro)
def financeiro(client, message: Message):
    message.reply_text(f"""
/faturamento_mk1 - Criar filtro de faturamento mk1
/faturamento_mk3 - Criar filtro de faturamento mk3
/relatorio_faturamento dd/mm/yyyy - relatório logs faturamento
""")

@app.on_message(filters.command("spc"))
@authorization(chat_mis)
def spc(client, message: Message):
    message.reply_text(f"""
/iniciar_include_spc - Iniciar inclusões no sistema spc
/parar_include_spc - Parar inclusões no sistema spc
/status_include_spc - Status inclusões no sistema spc
/relatorio_spc dd/mm/yyyy - relatório logs spc
""")

@app.on_message(filters.command("cancelamento"))
@authorization(chat_mis)
def cancelamento(client, message: Message):
    message.reply_text(f"""
/iniciar_cancelamento - Iniciar cancelamento
/parar_cancelamento - Parar cancelamento
/status_cancelamento - Status cancelamento
/relatorio_cancelamento dd/mm/yyyy - relatório logs cancelamento
""")

@app.on_message(filters.command("recolhimento"))
@authorization(chat_mis)
def cancelamento(client, message: Message):
    message.reply_text(f"""
/iniciar_recolhimento - Iniciar recolhimento
/parar_recolhimento - Parar recolhimento
/status_recolhimento - Status recolhimento
/relatorio_recolhimento dd/mm/yyyy - relatório logs recolhimento
""")

@app.on_message(filters.command("faturamento_mk1"))
@authorization(chat_financeiro)
def faturamento(client, message: Message):
    message.reply_text(f"""
/iniciar_faturamento_mk1 - Inciar faturamento mk1
/parar_faturamento_mk1 - Parar faturamento mk1
/status_faturamento_mk1 - Status faturamento mk1
""")

@app.on_message(filters.command("faturamento_mk3"))
@authorization(chat_financeiro)
def faturamento(client, message: Message):
    message.reply_text(f"""
/iniciar_faturamento_mk3 - Inciar faturamento mk3
/parar_faturamento_mk3 - Parar faturamento mk3
/status_faturamento_mk3 - Status faturamento mk3
""")

@app.on_message(filters.command("chat"))
def handle_chat_id(client, message: Message):
    message.reply_text(message.from_user.id)
    print(message.from_user.id)

############################################# SPC #############################################
# iniciar inclusões no sistema spc
@app.on_message(filters.command("iniciar_include_spc"))
@authorization(chat_mis)
def iniciar_include_spc(client: Client, message: Message):
    handle_start_include_spc(client, message)

# parar inclusões no sistema spc
@app.on_message(filters.command("parar_include_spc"))
@authorization(chat_mis)
def parar_include_spc(client: Client, message: Message):
    handle_stop_include_spc(client, message)

# status inclusões no sistema spc
@app.on_message(filters.command("status_include_spc"))
@authorization(chat_mis)
def status_include_spc(client: Client, message: Message):
    handle_status_include_spc(client, message)

# relatório de inclusões no sistema spc
@app.on_message(filters.command("relatorio_spc") & filters.text)
@authorization(chat_mis)
def report_spc(client: Client, message: Message):
    handle_report_spc(client, message)

############################################# CANCELLATION #############################################
# iniciar cancelamento no sistema mk
@app.on_message(filters.command("iniciar_cancelamento"))
@authorization(chat_mis)
def iniciar_cancellation(client: Client, message: Message):
    handle_start_cancellation_mk(client, message)

# parar cancelamento no sistema mk
@app.on_message(filters.command("parar_cancelamento"))
@authorization(chat_mis)
def parar_cancellation(client: Client, message: Message):
    handle_stop_cancellation_mk(client, message)

# status cancelamento no sistema mk
@app.on_message(filters.command("status_cancelamento"))
@authorization(chat_mis)
def status_cancellation(client: Client, message: Message):
    handle_status_cancellation_mk(client, message)

# relatório cancelamento no sistema mk
@app.on_message(filters.command("relatorio_cancelamento") & filters.text)
@authorization(chat_mis)
def report_cancellation(client: Client, message: Message):
    handle_report_cancellation(client, message)

############################################# RETREAT #############################################
# iniciar recolhimento no sistema mk
@app.on_message(filters.command("iniciar_recolhimento"))
@authorization(chat_mis)
def iniciar_retreat(client: Client, message: Message):
    handle_start_retreat_mk(client, message)

# parar recolhimento no sistema mk
@app.on_message(filters.command("parar_recolhimento"))
@authorization(chat_mis)
def parar_retreat(client: Client, message: Message):
    handle_stop_retreat_mk(client, message)

# status recolhimento no sistema mk
@app.on_message(filters.command("status_recolhimento"))
@authorization(chat_mis)
def status_retreat(client: Client, message: Message):
    handle_status_retreat_mk(client, message)

# relatório recolhimento no sistema mk
@app.on_message(filters.command("relatorio_recolhimento") & filters.text)
@authorization(chat_mis)
def report_retreat(client: Client, message: Message):
    handle_report_retreat(client, message)

############################################# INVOICING #############################################
# iniciar faturamento no sistema mk1
@app.on_message(filters.command("iniciar_faturamento_mk1"))
@authorization(chat_financeiro)
def iniciar_faturamento(client: Client, message: Message):
    handle_start_invoicing_mk1(client, message)

# parar faturamento no sistema mk1
@app.on_message(filters.command("parar_faturamento_mk1"))
@authorization(chat_financeiro)
def parar_faturamento(client: Client, message: Message):
    handle_stop_invoicing_mk1(client, message)

# status faturamento no sistema mk1
@app.on_message(filters.command("status_faturamento_mk1"))
@authorization(chat_financeiro)
def status_faturamento(client: Client, message: Message):
    handle_status_invoicing_mk1(client, message)

# iniciar faturamento no sistema mk3
@app.on_message(filters.command("iniciar_faturamento_mk3"))
@authorization(chat_financeiro)
def iniciar_faturamento(client: Client, message: Message):
    handle_start_invoicing_mk3(client, message)

# parar faturamento no sistema mk3
@app.on_message(filters.command("parar_faturamento_mk3"))
@authorization(chat_financeiro)
def parar_faturamento(client: Client, message: Message):
    handle_stop_invoicing_mk3(client, message)

# status faturamento no sistema mk3
@app.on_message(filters.command("status_faturamento_mk3"))
@authorization(chat_financeiro)
def status_faturamento(client: Client, message: Message):
    handle_status_invoicing_mk3(client, message)

# relatório faturamento no sistema mk
@app.on_message(filters.command("relatorio_faturamento") & filters.text)
@authorization(chat_financeiro)
def report_invoicing(client: Client, message: Message):
    handle_report_invoicing(client, message)


print("Serve Telegram Up!")
print(f"Version {version}")
app.run()
