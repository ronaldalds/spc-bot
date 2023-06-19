import time
from driver.mk.mk_driver import Mk
from driver.mk.coin.coin import Financeiro
from driver.mk.aside.aside_financeiro import Faturamento
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from driver.mk.mk_select import FATURAMENTO
import os
import logging
from datetime import datetime

load_dotenv()

SUCESS = 35
logging.addLevelName(SUCESS,'SUCESS')
    

def faturamento(
        mk,
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
    
    regra_faturamento = FATURAMENTO[regra]
    if mk == "test":
        instance = Mk(
            username=os.getenv('USERNAME_MK_TEST'),
            password=os.getenv('PASSWORD_MK_TEST'),
            url=os.getenv('URL_MK_TEST'),
        )
    elif mk == 1:
        instance = Mk(
            username=os.getenv('USERNAME_MK1'),
            password=os.getenv('PASSWORD_MK1'),
            url=os.getenv('URL_MK1'),
        )
    elif mk == 3:
        instance = Mk(
            username=os.getenv('USERNAME_MK3'),
            password=os.getenv('PASSWORD_MK3'),
            url=os.getenv('URL_MK3'),
        )
    else:
        logging.warning('Error na escolha do mk')

    financeiro = Financeiro()
    painel_faturamento = Faturamento()

    # login no mk
    try:
        instance.login()
    except:
        logging.error(f'Error login mk{mk}')
        instance.close()
        return
    
    instance.minimizeChat()

    # fechar tela de complete seu cadastro
    try:
        instance.iframeMain()
        instance.click('//div[@class="OptionClose"]')
    except:
        print(f"Sem tela de complete seu cadastro MK{mk}")
    
    # click na moeda financeiro
    instance.iframeCoin()
    instance.click(financeiro.xpath())

    # click aside faturamento
    instance.iframeAsideCoin(financeiro)
    instance.click(painel_faturamento.xpath())

    # click adicionar novo faturamento
    instance.iframePainel(financeiro, painel_faturamento)
    instance.click('//*[@title="Novo faturamento..."]')

    # select regra de vencimento
    try:
        instance.iframeForm()
        instance.click('//*[@title="Selecione a regra de faturamento desejada."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', regra + Keys.ENTER)
        instance.click(f'//option[@value="{regra_faturamento}"]')
    except:
        logging.error(f'Error regra de vencimento {regra} MK{mk}')
        instance.close()
        return
    
    # Data Inicial
    try:
        instance.write('//*[@title="Data de vencimento inicial das contas que devem ser faturadas."]', data_inicial)
    except:
        logging.error(f'Error data inicial {data_inicial} MK{mk}')
        instance.close()
        return
    
    # Data final
    try:
        instance.write('//*[@title="Data de vencimento final das contas que devem ser faturadas."]', data_final)
    except:
        logging.error(f'Error data final {data_final} MK{mk}')
        instance.close()
        return
    
    # vencimento
    try:
        instance.write('//*[@title="Data de vencimento da fatura que será criada."]', data_vecimento)
    except:
        logging.error(f'Error data vencimento {data_vecimento} MK{mk}')
        instance.close()
        return
    
    # confirma geração
    try:
        instance.click('//*[@title="Clique para confirmar a geração da prévia de faturamento."]/input[2]')
    except:
        logging.error(f'Error click checkbox confirma geração MK{mk}')
        instance.close()
        return
    
    # executar filtro de faturamento
    try:
        instance.click('//*[@title="Clique para executar o filtro deste novo faturamento."]')
    except:
        logging.error(f'Error click botão de executar filtro de faturamento MK{mk}')
        instance.close()
        return

    # alert filtro aplicado
    instance.include()

    # dbclick novo filtro
    try:
        instance.iframeGridFaturamento(financeiro, painel_faturamento)
        instance.dbclick(f'//div[@aria-rowindex="1" and @aria-colindex="5"]')
    except:
        logging.warning(f'Filtro regra {regra} no MK{mk} não encontrado')
        instance.close()
        return

    # marca todos
    # try:
    #     instance.iframeGridResFaturamento(financeiro, painel_faturamento)
    #     instance.click(f'//input[@id="rowselectAll"]')
    # except:
    #     logging.warning(f'Filtro regra {regra} no MK{mk} não encontrado')
    #     instance.close()
    #     return

    # click ignorar faturamento
    instance.iframePainel(financeiro, painel_faturamento)
    instance.click('//*[@title="Ignorar contas para o faturamento."]')

    # select Profile
    # try:
    #     instance.iframeGridResFaturamento(financeiro, painel_faturamento)
    #     instance.write(f'//td[@column="10" and @class=" webix_last_row"]/div/input', "Bradesco")
    # except:
    #     logging.warning(f'Filtro Profile no MK{mk} não encontrado')
    #     instance.close()
    #     return

    # marca todos
    # try:
    #     instance.iframeGridResFaturamento(financeiro, painel_faturamento)
    #     instance.click(f'//input[@id="rowselectAll"]')
    # except:
    #     logging.warning(f'Filtro regra {regra} no MK{mk} não encontrado')
    #     instance.close()
    #     return

    # click habilitar faturamento
    instance.iframePainel(financeiro, painel_faturamento)
    instance.click('//*[@title="Reabilitar contas para o faturamento."]')

    time.sleep(10)
    instance.close()