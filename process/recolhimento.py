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

def recolhimento(
        mk,
        contrato,
        conexao_associada,
        cpf,
        cod,
        tipo_da_os,
        grupo_atendimento_os,
        detalhe_os,
        loja
        ):
    print(f'Iniciou recolhimento contrato: {contrato} cpf: {cpf} loja:{loja} MK:{mk}.')

    # configuração logs
    SUCESS = 35
    logging.addLevelName(SUCESS,'SUCESS')
    file_log_recolhimento = datetime.now().strftime("recolhimento_%Y-%m-%d.log")
    logging.basicConfig(level=logging.WARNING)
    logger_recolhimento = logging.getLogger("recolhimento")
    formatter = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
    file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'logs', file_log_recolhimento))
    file_handler.setFormatter(formatter)
    logger_recolhimento.addHandler(file_handler)
    prefixo_log_recolhimento = f'MK:{mk} contrato:{contrato} conexão:{conexao_associada} cpf:{cpf}'

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
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Não foi possível criar instancia do mk...')
    
    
    workspace = Workspace()
    ospainel = OsPainel()

    # login no sistema mk
    try:
        instance.login()
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Failed to login')
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
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Identificador O.S Nome / Documento / Código')
        instance.close()
        return

    # Avançar no assistente de O.S primeira tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[2]//button[@title="Avançar no assistente de O.S."]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Avançar no assistente de O.S primeira tela')
        instance.close()
        return
    
    # Escolha de conexão Conexão Associada
    try:
        instance.iframeForm()
        instance.click('//*[@title="Neste campo é informado para qual conexão foi aberta esta Ordem de Serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{conexao_associada}" + Keys.ENTER)
        instance.click(f'//option[@value="{conexao_associada}"]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Escolha de conexão Conexão Associada')
        instance.close()
        return
    
    # Escolha nivel de SLA se habilitado
    try:
        time.sleep(5)
        instance.iframeForm()
        instance.click('//*[@title="Escolhe o nível de prioridade deste serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', "Preventivo" + Keys.ENTER)
        instance.click(f'//option[@value="{valor_nivel_sla}"]')
    except:
        logger_recolhimento.warning(f'{prefixo_log_recolhimento} - Escolha nivel de SLA se habilitado')

    # Avançar no assistente de O.S segunda tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[3]//button[@title="Avançar no assistente de O.S."]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Avançar no assistente de O.S segunda tela')
        instance.close()
        return

    # Escolha tipo de O.S
    try:
        instance.iframeForm()
        instance.click('//*[@title="Informa qual o tipo da Ordem de Serviço."]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{tipo_da_os}" + Keys.ENTER)
        instance.click(f'//option[@value="{valor_tipo_de_os}"]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Escolha tipo de O.S')
        instance.close()
        return

    # Escrever Relato do problema
    try:
        instance.iframeForm()
        instance.write('//textarea[@title="Neste campo é informado o relato do cliente perante a abertura da Ordem de Serviço."]', detalhe_os)
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Escrever Relato do problema')
        instance.close()
        return

    # Avançar no assistente de O.S terceira tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[4]//button[@title="Avançar no assistente de O.S."]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Avançar no assistente de O.S terceira tela')
        instance.close()
        return
    
    # Avançar no assistente de O.S quarta tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[8]//button[@title="Avançar no assistente de O.S."]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Avançar no assistente de O.S quarta tela')
        instance.close()
        return


    # Escolha Grupo de atendimento
    try:
        instance.iframeForm()
        instance.click('//div[@class="HTMLTabContainer"]/div[9]//div[@class="HTMLLookup"]/div[2]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{grupo_atendimento_os}" + Keys.ENTER)
        instance.click(f'//option[@value="{valor_grupo_atendimento}"]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Escolha Grupo de atendimento')
        instance.close()
        return

    # Avançar no assistente de O.S quinta tela
    try:
        instance.click('//div[@class="HTMLTabContainer"]/div[9]//button[@title="Avançar no assistente de O.S."]')
    except:
        logger_recolhimento.error(f'{prefixo_log_recolhimento} - Avançar no assistente de O.S quinta tela')
        instance.close()
        return

    # Avançar no assistente de O.S sexta tela
    # try:
    #     instance.click('//div[@class="HTMLTabContainer"]/div[10]//button[@title="Clique para efetivar a criação desta O.S.."]')
    # except:
    #     logger_recolhimento.error(f'{prefixo_log_recolhimento} - Avançar no assistente de O.S sexta tela')
    #     instance.close()
    #     return

    # alert concluir O.S recolhimento
    # instance.include()

    # log recolhimento de contrato conluído
    logger_recolhimento.log(SUCESS, f'{prefixo_log_recolhimento} - recolhimento de contrato conluído')

    time.sleep(10)
    instance.close()