from pyrogram import Client, filters
import os
from pyrogram.types import Message
from dotenv import load_dotenv
from service.service_spc import handle_processar_include_spc
from driver.mk.aside.aside_estoque import EstoqueHome

load_dotenv()

app = Client(
    name=os.getenv("BOT_NAME_TELEGRAM"), 
    api_hash=os.getenv("API_HASH_TELEGRAM"),
    api_id=os.getenv("API_ID_TELEGRAM"),
    bot_token=os.getenv("BOT_TOKEN_TELEGRAM")
    )

@app.on_message(filters.command("start"))
def process(client, message: Message):
    message.reply_text(f"""
/mis - comando para setor MIS
/ost - comando para setor OST
/chat - Para informa seu chat_id
""")

@app.on_message(filters.command("ost"))
def process(client, message: Message):
    message.reply_text(f"""
/verificar - Verifica O.S de 
""")

@app.on_message(filters.command("mis"))
def process(client, message: Message):
    message.reply_text(f"""
/includespc - Inclui clientes no sistema do spc
/cancelamento - Cancelamento de cliente mk
/recolhimento - Cria O.S de Recolhimento no mk
""")

@app.on_message(filters.command("chat"))
def handle_chat_id(client, message):
    message.reply_text(message.from_user.id)

# incluir clientes no sistema do spc
app.on_message(filters.command("includespc"))(handle_processar_include_spc)

app.run()