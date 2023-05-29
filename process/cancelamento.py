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

file_log = datetime.now().strftime("cancelamento_%d_%m_%Y.log")
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), 'logs', file_log),
    encoding='utf-8',
    filemode='a',
    format='%(levelname)s - %(asctime)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.WARNING
)

SUCESS = 35
logging.addLevelName(SUCESS,'SUCESS')

def cancelamento(
        mk,
        cod_pessoa,
        contrato,
        detalhes_cancelamento,
        tipo_da_os,
        grupo_atendimento_os,
        relato_do_problema,

        # dados para multa
        incidencia_multa,
        valor_multa,
        vencimento_multa,
        planos_contas
        ):

    if mk == 1:
        instance = Mk(
            username=os.getenv('USERNAME_MK_TEST'),
            password=os.getenv('PASSWORD_MK_TEST'),
            url=os.getenv('URL_MK_TEST'),
        )
    else:
        print('error: mk')
        # instance = Mk(
        #     username=os.getenv('URL_MK3'),
        #     password=os.getenv('USERNAME_MK3'),
        #     url=os.getenv('PASSWORD_MK3'),
        # )

    financeiro = Financeiro()
    painel_do_cliente = PainelDoCliente()

    instance.login()

    # click na moeda financeiro
    instance.iframeCoin()
    instance.click(financeiro.xpath())

    instance.minimizeChat()

    # click aside Painel do cliente
    instance.iframeAsideCoin(financeiro)
    instance.click(painel_do_cliente.xpath())

    # click pesquisa avançada
    instance.iframePainel(financeiro, painel_do_cliente)
    instance.click('//*[@title="Clique para fazer uma pesquisa avançada de clientes ou fornecedores"]')

    # pesquisar por Código de cadastro
    instance.click('//*[@class="HTMLComboBox"]/div[1]/div/button')

    time.sleep(10)
    instance.close()

