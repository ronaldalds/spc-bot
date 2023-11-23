import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Src.Middleware.authentication import authorization
from Src.Controller.spc_controller import handle_start_include_spc, handle_stop_include_spc, handle_status_include_spc

load_dotenv()

version = "0.0.5"

app = Client(
    name="incluir_spc_bot", 
    api_hash=os.getenv("API_HASH_TELEGRAM"),
    api_id=os.getenv("API_ID_TELEGRAM"),
    bot_token=os.getenv("BOT_TOKEN_TELEGRAM")
    )

@app.on_message(filters.command("start"))
def start(client: Client, message: Message):
    message.reply_text(f"""
/spc - Inclui clientes no sistema do spc
/chat - Informa seu chat_id
/chatgroup - Informa chat_id grupo
""")

@app.on_message(filters.command("spc"))
@authorization()
def spc(client, message: Message):
    message.reply_text(f"""
/iniciar_include_spc - Iniciar inclusões no sistema spc
/parar_include_spc - Parar inclusões no sistema spc
/status_include_spc - Status inclusões no sistema spc
""")
    
@app.on_message(filters.command("chatgroup"))
@authorization()
def handle_chatgroup_id(client: Client, message: Message):
    client.send_message(message.from_user.id, message)

@app.on_message(filters.command("chat"))
def handle_chat_id(client: Client, message: Message):
    text = f"{message.from_user.first_name}.{message.from_user.last_name} - ID:{message.from_user.id}"
    client.send_message(message.from_user.id, text)
    if int(os.getenv("CHAT_ID_ADM")) != message.from_user.id:
        client.send_message(int(os.getenv("CHAT_ID_ADM")), text)

# iniciar inclusões no sistema spc
@app.on_message(filters.command("iniciar_include_spc"))
@authorization()
def iniciar_include_spc(client: Client, message: Message):
    handle_start_include_spc(client, message)

# parar inclusões no sistema spc
@app.on_message(filters.command("parar_include_spc"))
@authorization()
def parar_include_spc(client: Client, message: Message):
    handle_stop_include_spc(client, message)

# status inclusões no sistema spc
@app.on_message(filters.command("status_include_spc"))
@authorization()
def status_include_spc(client: Client, message: Message):
    handle_status_include_spc(client, message)

# stop service
@app.on_message(filters.command("stop_service"))
@authorization()
def stop(client: Client, message: Message):
    print("Service Stopping")
    app.stop()

print("Service Telegram Up!")
print(f"Version {version}")
app.run()

