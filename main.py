from pyrogram import Client, filters
import os
from pyrogram.types import Message
from dotenv import load_dotenv
from service.service_spc import handle_start_include_spc, handle_stop_include_spc, handle_status_include_spc
from service.service_cancellation import handle_start_cancellation_mk, handle_stop_cancellation_mk, handle_status_cancellation_mk
from service.service_retreat import handle_start_retreat_mk, handle_stop_retreat_mk, handle_status_retreat_mk
from service.service_x9 import handle_start_x9_mk1, handle_stop_x9_mk1, handle_status_x9_mk1
from service.service_report import handle_report
from service.service_invoicing import (
    handle_start_invoicing_mk1,
    handle_stop_invoicing_mk1,
    handle_status_invoicing_mk1,
    handle_start_invoicing_mk3,
    handle_stop_invoicing_mk3,
    handle_status_invoicing_mk3
    )

load_dotenv()

version = "0.0.5"

app = Client(
    name=os.getenv("BOT_NAME_TELEGRAM"), 
    api_hash=os.getenv("API_HASH_TELEGRAM"),
    api_id=os.getenv("API_ID_TELEGRAM"),
    bot_token=os.getenv("BOT_TOKEN_TELEGRAM")
    )

chat_re = [
    os.getenv("CHAT_ID_ADM"),
    os.getenv("CHAT_ID_ADM_MK"),
    os.getenv("CHAT_ID_SPC"),
    os.getenv("CHAT_ID_CANCELAMENTO"),
    os.getenv("CHAT_ID_RECOLHIMENTO"),
    os.getenv("CHAT_ID_INFRA"),
    os.getenv("CHAT_ID_GESTOR_MIS"),
    os.getenv("CHAT_ID_GESTOR_INFRA"),
    os.getenv("CHAT_ID_LOGISTICA"),
    ]

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

chat_adm = [
    os.getenv("CHAT_ID_ADM")
    ]

chat_financeiro = [
    os.getenv("CHAT_ID_ADM"),
    os.getenv("CHAT_ID_ADM_MK"),
    ]

chat_logistica = [
    os.getenv("CHAT_ID_ADM"),
    os.getenv("CHAT_ID_INFRA"),
    os.getenv("CHAT_ID_GESTOR_INFRA"),
    os.getenv("CHAT_ID_LOGISTICA"),
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

@app.on_message(filters.command("chatgroup"))
def handle_chatgroup_id(client: Client, message: Message):
    client.send_message(-1001550273372, message)

@app.on_message(filters.command("start"))
@authorization(chat_re)
def start(client, message: Message):
    message.reply_text(f"""
/mis - Setor MIS
/ost - Setor OST
/financeiro - Setor Financeiro
/logistica - Setor Logistica
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
/relatorio dd/mm/yyyy - Relatorio logs
""")
    
@app.on_message(filters.command("financeiro"))
@authorization(chat_financeiro)
def financeiro(client, message: Message):
    message.reply_text(f"""
/faturamento_mk1 - Criar filtro de faturamento mk1
/faturamento_mk3 - Criar filtro de faturamento mk3
""")
    
@app.on_message(filters.command("logistica"))
@authorization(chat_logistica)
def financeiro(client, message: Message):
    message.reply_text(f"""
/iniciar_x9 - Iniciar x9
/parar_x9 - Parar x9
/status_x9 - Status x9
""")

@app.on_message(filters.command("spc"))
@authorization(chat_mis)
def spc(client, message: Message):
    message.reply_text(f"""
/iniciar_include_spc - Iniciar inclusões no sistema spc
/parar_include_spc - Parar inclusões no sistema spc
/status_include_spc - Status inclusões no sistema spc
""")

@app.on_message(filters.command("cancelamento"))
@authorization(chat_mis)
def cancelamento(client, message: Message):
    message.reply_text(f"""
/iniciar_cancelamento - Iniciar cancelamento
/parar_cancelamento - Parar cancelamento
/status_cancelamento - Status cancelamento
""")

@app.on_message(filters.command("recolhimento"))
@authorization(chat_mis)
def cancelamento(client, message: Message):
    message.reply_text(f"""
/iniciar_recolhimento - Iniciar recolhimento
/parar_recolhimento - Parar recolhimento
/status_recolhimento - Status recolhimento
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
def handle_chat_id(client: Client, message: Message):
    client.send_message(message.from_user.id, message.from_user.id,)
    print(message.from_user.id)

# relatórios
@app.on_message(filters.command("relatorio") & filters.text)
@authorization(chat_re)
def report(client: Client, message: Message):
    handle_report(client, message)

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

# stop service
@app.on_message(filters.command("stop_service"))
@authorization(chat_adm)
def stop(client: Client, message: Message):
    print("Service Stopping")
    app.stop()

print("Service Telegram Up!")
print(f"Version {version}")
app.run()

