import time
from driver.mk.mk_driver import Mk
from driver.mk.coin.coin import Workspace
from driver.mk.aside.aside_workspace import OsPainel
from selenium.webdriver.common.keys import Keys
from driver.mk.mk_select import (
    TIPO_DA_OS,
    NIVEL_DE_SLA,
    GRUPO_DE_ATENDIMENTO_TEST,
    GRUPO_DE_ATENDIMENTO_MK01,
    GRUPO_DE_ATENDIMENTO_MK03
)
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

SUCESS = 35
logging.addLevelName(SUCESS,'SUCESS')

def recolhimento(
        mk,
        contrato,
        conexao_associada,
        cpf,
        cod,
        tipo_da_os,
        grupo_atendimento_os,
        detalhe_os
        ):
    print(f'Iniciou recolhimento contrato: {contrato} cpf: {cpf} no MK:{mk}.')
    file_log = datetime.now().strftime("recolhimento_%Y-%m-%d.log")
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(__file__), 'logs', file_log),
        encoding='utf-8',
        filemode='a',
        format='%(levelname)s - %(asctime)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.WARNING
        )

    valor_nivel_sla = NIVEL_DE_SLA['Preventivo']
    valor_tipo_de_os = TIPO_DA_OS[tipo_da_os]
    if mk == "test":
        instance = Mk(
            username=os.getenv('USERNAME_MK_TEST'),
            password=os.getenv('PASSWORD_MK_TEST'),
            url=os.getenv('URL_MK_TEST'),
        )
        valor_grupo_atendimento = GRUPO_DE_ATENDIMENTO_TEST[grupo_atendimento_os]
    elif mk == 1:
        instance = Mk(
            username=os.getenv('USERNAME_MK1'),
            password=os.getenv('PASSWORD_MK1'),
            url=os.getenv('URL_MK1'),
        )
        valor_grupo_atendimento = GRUPO_DE_ATENDIMENTO_MK01[grupo_atendimento_os]
    elif mk == 3:
        instance = Mk(
            username=os.getenv('USERNAME_MK3'),
            password=os.getenv('PASSWORD_MK3'),
            url=os.getenv('URL_MK3'),
        )
        valor_grupo_atendimento = GRUPO_DE_ATENDIMENTO_MK03[grupo_atendimento_os]

    else:
        logging.warning('Error na escolha do mk')
    
    workspace = Workspace()
    ospainel = OsPainel()

    try:
        # login no sistema mk
        instance.login()
    except:
        logging.error(f'Failed to login MK{mk}')
        instance.close()
        return

    instance.minimizeChat()

    # fechar tela de complete seu cadastro
    try:
        instance.iframeMain()
        instance.click('//div[@class="OptionClose"]')
    except:
        pass

    # click na moeda workspace
    instance.iframeCoin()
    instance.click(workspace.xpath())

    # click aside O.S - Painel
    instance.iframeAsideCoin(workspace)
    instance.click(ospainel.xpath())

    # click criar nova O.S
    instance.iframePainel(workspace, ospainel)
    instance.click('//*[@title="Criar Nova O.S."]')

    # Identificador O.S Nome / Documento / Código
    try:
        instance.iframeForm()
        instance.click('//*[@title="Este campo informa qual é o cliente associado a esta Ordem de Serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{cpf}" + Keys.ENTER)
        instance.click(f'//option[@value="{cod}"]')
    except:
        logging.error(f'Error documento cpf:{cpf} ou código:{cod} MK{mk}')
        instance.close()
        return

    # Avançar no assistente de O.S primeira tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[2]//button[@title="Avançar no assistente de O.S."]')
    except:
        logging.error(f'Error Avançar no assistente identificador O.S primeira tela MK{mk}')
        instance.close()
        return
    
    # Escolha de conexão Conexão Associada
    try:
        instance.iframeForm()
        instance.click('//*[@title="Neste campo é informado para qual conexão foi aberta esta Ordem de Serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{conexao_associada}" + Keys.ENTER)
        instance.click(f'//option[@value="{conexao_associada}"]')
    except:
        logging.error(f'Error conexão:{conexao_associada} MK{mk}')
        instance.close()
        return
    
    # Escolha nivel de SLA se habilitado
    try:
        instance.iframeForm()
        instance.click('//*[@title="Escolhe o nível de prioridade deste serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', "Preventivo" + Keys.ENTER)
        instance.click(f'//option[@value="{valor_nivel_sla}"]')
    except:
        logging.warning(f'Nível de SLA não habilitado na conexão:{conexao_associada} MK{mk}')

    # Avançar no assistente de O.S segunda tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[3]//button[@title="Avançar no assistente de O.S."]')
    except:
        logging.error(f'Error Avançar no assistente identificador O.S segunda tela MK{mk}')
        instance.close()
        return

    # Escolha tipo de O.S
    try:
        instance.iframeForm()
        instance.click('//*[@title="Informa qual o tipo da Ordem de Serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{tipo_da_os}" + Keys.ENTER)
        instance.click(f'//option[@value="{valor_tipo_de_os}"]')
    except:
        logging.error(f'Error tipo de os:{tipo_da_os} MK{mk}')
        instance.close()
        return

    # Escrever Relato do problema
    try:
        instance.iframeForm()
        instance.write('//textarea[@title="Neste campo é informado o relato do cliente perante a abertura da Ordem de Serviço."]', detalhe_os)
    except:
        logging.error(f'Error detalhe da os MK{mk}')
        instance.close()
        return

    # Avançar no assistente de O.S terceira tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[4]//button[@title="Avançar no assistente de O.S."]')
    except:
        logging.error(f'Error Avançar no assistente identificador O.S terceira tela MK{mk}')
        instance.close()
        return

    # log recolhimento de contrato conluído
    logging.log(SUCESS, f"Recolhimento do contrato:{contrato} conexao:{conexao_associada} MK{mk} concluído.")

    time.sleep(10)
    instance.close()