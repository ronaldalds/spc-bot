from pyrogram import Client, filters
import os
from pyrogram.types import Message
import multiprocessing
from dotenv import load_dotenv
from service.service_spc import handle_processar_include_spc

load_dotenv()

app = Client(
    name=os.getenv("BOT_NAME_TELEGRAM"), 
    api_hash=os.getenv("API_HASH_TELEGRAM"),
    api_id=os.getenv("API_ID_TELEGRAM"),
    bot_token=os.getenv("BOT_TOKEN_TELEGRAM")
    )
num_process = multiprocessing.cpu_count()



# incluir clientes no sistema do spc
app.on_message(filters.command("includespc"))(handle_processar_include_spc)




@app.on_message()
def process(client, message: Message):
    message.reply_text(f"""
/includespc - Inclui clientes no sistema do spc
/cancelamento - Cancelamento de cliente mk
/recolhimento - Cria O.S de Recolhimento no mk
""")

app.run()