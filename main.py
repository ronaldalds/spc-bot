from pyrogram import Client, filters
import os
from pyrogram.types import Message
from dotenv import load_dotenv
from service.service_spc import handle_include_spc
from service.service_cancellation_mk import handle_start_cancellation_mk, handle_stop_cancellation_mk, handle_status_cancellation_mk
from service.service_report import handle_report_cancellation, handle_report_spc, handle_report_invoicing
from service.service_invoicing import handle_start_invoicing, handle_stop_invoicing, handle_status_invoicing

load_dotenv()

version = "0.0.1"

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
""")
    
@app.on_message(filters.command("financeiro"))
@authorization(chat_financeiro)
def financeiro(client, message: Message):
    message.reply_text(f"""
/faturamento - Criar filtro de faturamento
""")

@app.on_message(filters.command("spc"))
@authorization(chat_mis)
def spc(client, message: Message):
    message.reply_text(f"""
/include_spc - Inclui clientes no sistema do spc
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

@app.on_message(filters.command("faturamento"))
@authorization(chat_mis)
def faturamento(client, message: Message):
    message.reply_text(f"""
/iniciar_faturamento - Inciar faturamento
/parar_faturamento - Parar faturamento
/status_faturamento - Status faturamento
/relatorio_faturamento dd/mm/yyyy - relatório logs faturamento
""")

@app.on_message(filters.command("chat"))
def handle_chat_id(client, message: Message):
    message.reply_text(message.from_user.id)
    print(message.from_user.id)

############################################# SPC #############################################
# incluir clientes no sistema do spc
@app.on_message(filters.command("include_spc"))
@authorization(chat_mis)
def include_spc(client: Client, message: Message):
    handle_include_spc(client, message)

# relatório de inclusões no sistema spc
@app.on_message(filters.command("relatorio_spc") & filters.text)
@authorization(chat_mis)
def report_spc(client: Client, message: Message):
    handle_report_spc(client, message)

############################################# CANCELLATION #############################################
# cancelar contrato no sistema mk
@app.on_message(filters.command("iniciar_cancelamento"))
@authorization(chat_mis)
def iniciar_cancellation(client: Client, message: Message):
    handle_start_cancellation_mk(client, message)

# start running invoicing
@app.on_message(filters.command("parar_cancelamento"))
@authorization(chat_mis)
def parar_cancellation(client: Client, message: Message):
    handle_stop_cancellation_mk(client, message)

# stop running invoicing
@app.on_message(filters.command("status_cancelamento"))
@authorization(chat_mis)
def status_cancellation(client: Client, message: Message):
    handle_status_cancellation_mk(client, message)

# relatório cancelamentos no sistema mk
@app.on_message(filters.command("relatorio_cancelamento") & filters.text)
@authorization(chat_mis)
def report_cancellation(client: Client, message: Message):
    handle_report_cancellation(client, message)

############################################# INVOICING #############################################
# start running invoicing
@app.on_message(filters.command("iniciar_faturamento"))
@authorization(chat_financeiro)
def iniciar_faturamento(client: Client, message: Message):
    handle_start_invoicing(client, message)

# stop running invoicing
@app.on_message(filters.command("parar_faturamento"))
@authorization(chat_financeiro)
def parar_faturamento(client: Client, message: Message):
    handle_stop_invoicing(client, message)

# status invoicing
@app.on_message(filters.command("status_faturamento"))
@authorization(chat_financeiro)
def status_faturamento(client: Client, message: Message):
    handle_status_invoicing(client, message)

# relatório faturamento no sistema mk
@app.on_message(filters.command("relatorio_faturamento") & filters.text)
@authorization(chat_financeiro)
def report_invoicing(client: Client, message: Message):
    handle_report_invoicing(client, message)

print("Serve Telegram Up!")
print(f"Version {version}")
app.run()
