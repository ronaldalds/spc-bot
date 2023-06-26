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

def faturamento(
        mk,
        regra,
        data_inicial,
        data_final,
        data_vecimento
        ):
    
    # configuração logs
    SUCESS = 35
    logging.addLevelName(SUCESS,'SUCESS')
    file_log_faturamento = datetime.now().strftime("faturamento_%Y-%m-%d.log")
    logging.basicConfig(
        level=logging.WARNING,
        filename=os.path.join(os.path.dirname(__file__), 'logs', file_log_faturamento),
        format='%(levelname)s - %(name)s - %(asctime)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        encoding='utf-8',
        filemode='a'
        )
    logger_faturamento = logging.getLogger("faturamento")
    # formatter = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
    # file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'logs', file_log_faturamento))
    # file_handler.setFormatter(formatter)
    # logger_faturamento.addHandler(file_handler)
    prefixo_log_faturamento = f'MK:{mk} regra:{regra} datainicial:{data_inicial} data final:{data_final} vencimento:{data_vecimento}'
    
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
        logger_faturamento.error(f'{prefixo_log_faturamento} - Não foi possível criar instancia do mk...')

    financeiro = Financeiro()
    painel_faturamento = Faturamento()

    # login no mk
    try:
        instance.login()
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - login no mk')
        instance.close()
        return False
    
    instance.minimizeChat()

    # fechar tela de complete seu cadastro
    try:
        instance.iframeMain()
        instance.click('//div[@class="OptionClose"]')
    except:
        pass
    
    # click na moeda financeiro
    instance.iframeCoin()
    instance.click(financeiro.xpath())

    # click aside faturamento
    instance.iframeAsideCoin(financeiro)
    instance.click(painel_faturamento.xpath())

    # click adicionar novo faturamento
    instance.iframePainel(financeiro, painel_faturamento)
    instance.click('//*[@title="Novo faturamento..."]')

    # seleciona regra de vencimento
    try:
        instance.iframeForm()
        instance.click('//*[@title="Selecione a regra de faturamento desejada."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', regra + Keys.ENTER)
        instance.click(f'//option[@value="{regra_faturamento}"]')
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - seleciona regra de vencimento')
        instance.close()
        return False
    
    # Data Inicial
    try:
        instance.write('//*[@title="Data de vencimento inicial das contas que devem ser faturadas."]', data_inicial)
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - Data Inicial')
        instance.close()
        return False
    
    # Data final
    try:
        instance.write('//*[@title="Data de vencimento final das contas que devem ser faturadas."]', data_final)
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - Data final')
        instance.close()
        return False
    
    # Data vencimento
    try:
        instance.write('//*[@title="Data de vencimento da fatura que será criada."]', data_vecimento)
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - Data vencimento')
        instance.close()
        return False
    
    # click checkbox confirma geração de filtro de faturamento
    try:
        instance.click('//*[@title="Clique para confirmar a geração da prévia de faturamento."]/input[2]')
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - click checkbox confirma geração de filtro de faturamento')
        instance.close()
        return False
    
    # executar filtro de faturamento
    try:
        instance.click('//*[@title="Clique para executar o filtro deste novo faturamento."]')
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - executar filtro de faturamento')
        instance.close()
        return False

    # alert filtro aplicado
    instance.include()

    # dbclick novo filtro
    try:
        instance.iframeGridFaturamento(financeiro, painel_faturamento)
        instance.dbclick(f'//div[@aria-rowindex="1" and @aria-colindex="5"]')
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - dbclick novo filtro')
        instance.close()
        return False

    # marca todos para ignorar
    try:
        instance.iframeGridResFaturamento(financeiro, painel_faturamento)
        instance.click(f'//input[@id="rowselectAll"]')
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - marca todos para ignorar')
        instance.close()
        return False

    # click ignorar faturamento
    instance.iframePainel(financeiro, painel_faturamento)
    instance.click('//*[@title="Ignorar contas para o faturamento."]')

    # alert todos ignorados
    instance.include()

    # selecionar todos os Profile com Boleto Digital
    try:
        instance.iframeGridResFaturamento(financeiro, painel_faturamento)
        instance.write(f'//td[@column="10" and @class=" webix_last_row"]/div/input', "Boleto Digital")
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - selecionar todos os Profile com Boleto Digital')
        instance.close()
        return False

    # marca todos para habilitar faturamento com Boleto Digital
    try:
        instance.iframeGridResFaturamento(financeiro, painel_faturamento)
        instance.dbclick(f'//input[@id="rowselectAll"]')
    except:
        logger_faturamento.error(f'{prefixo_log_faturamento} - marca todos para habilitar faturamento com Boleto Digital')
        instance.close()
        return False

    # click habilitar faturamento
    instance.iframePainel(financeiro, painel_faturamento)
    instance.click('//*[@title="Reabilitar contas para o faturamento."]')

    # alert de tirar o ignorar do Boleto Digital
    instance.include()

    # log faturamento concluído
    logger_faturamento.log(SUCESS, f'{prefixo_log_faturamento} - faturamento concluído')

    time.sleep(10)
    instance.close()

    return True