from pyrogram import Client, filters
import os
from pyrogram.types import Message
from dotenv import load_dotenv
from service.service_spc import handle_include_spc
from service.service_cancelamento_mk import handle_cancelamento_mk
from service.service_relatorio import handle_relatorio_cancelamento, handle_relatorio_spc


load_dotenv()

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

# Verificação de autorização
def autorizado(ids_autorizados):
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
/mis - comando para setor MIS
/ost - comando para setor OST
/chat - Para informa seu chat_id
""")

@app.on_message(filters.command("ost"))
def ost(client, message: Message):
    message.reply_text(f"""
/verificar - Verifica O.S de 
""")

@app.on_message(filters.command("mis"))
def mis(client, message: Message):
    message.reply_text(f"""
/includespc - Inclui clientes no sistema do spc
/cancelamento - Cancelamento de cliente mk
/recolhimento - Cria O.S de Recolhimento no mk
""")

@app.on_message(filters.command("chat"))
def handle_chat_id(client, message: Message):
    message.reply_text(message.from_user.id)
    print(message.from_user.id)

# incluir clientes no sistema do spc

@app.on_message(filters.command("includespc"))
@autorizado(chat_mis)
def includespc(client: Client, message: Message):
    handle_include_spc(client, message)

# relatório de inclusões no sistema spc
@app.on_message(filters.command("relatorio-spc") & filters.text)
@autorizado(chat_mis)
def relatori_spc(client: Client, message: Message):
    handle_relatorio_spc(client, message)

# cancelar contrato no sistema mk
@app.on_message(filters.command("cancelamento"))
@autorizado(chat_mis)
def cancelamento(client: Client, message: Message):
    handle_cancelamento_mk(client, message)

# relatório cancelamentos no sistema mk
@app.on_message(filters.command("relatorio-cancelamento") & filters.text)
@autorizado(chat_mis)
def relatorio_cancelamento(client: Client, message: Message):
    handle_relatorio_cancelamento(client, message)


print("Serve Telegram Up!")
app.run()
