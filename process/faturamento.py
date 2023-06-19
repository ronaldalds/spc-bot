import time
from driver.mk.mk_driver import Mk
from driver.mk.coin.coin import Financeiro
from driver.mk.aside.aside_financeiro import PainelDoCliente
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

SUCESS = 35
logging.addLevelName(SUCESS,'SUCESS')
    

def faturamento(
        regra,
        data_inicial,
        data_final,
        data_vecimento
        ):
    print(f"regra {regra}")
    print(f"data atual {data_inicial}")
    print(f"data final {data_final}")
    print(f"data vencimento {data_vecimento}")
    file_log = datetime.now().strftime("faturamento_%Y-%m-%d.log")
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(__file__), 'logs', file_log),
        encoding='utf-8',
        filemode='a',
        format='%(levelname)s - %(asctime)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.WARNING
        )