import time
from driver.mk.mk_driver import Mk
from driver.mk.coin.coin import Financeiro
from driver.mk.aside.aside_financeiro import PainelDoCliente
from selenium.webdriver.common.keys import Keys
from driver.mk.mk_select import (
    TIPO_DA_OS,
    DEFEITO,
    MOTIVO_DE_CANCELAMENTO_TEST,
    MOTIVO_DE_CANCELAMENTO_MK01,
    MOTIVO_DE_CANCELAMENTO_MK03,
    GRUPO_DE_ATENDIMENTO_TEST,
    GRUPO_DE_ATENDIMENTO_MK01,
    GRUPO_DE_ATENDIMENTO_MK03
)
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

    if mk == "test":
        instance = Mk(
            username=os.getenv('USERNAME_MK_TEST'),
            password=os.getenv('PASSWORD_MK_TEST'),
            url=os.getenv('URL_MK_TEST'),
        )
        motivo_de_cancelamento  = MOTIVO_DE_CANCELAMENTO_TEST["Inadimplência"]
        valor_tipo_de_os = TIPO_DA_OS[tipo_da_os]
        valor_grupo_atendimento = GRUPO_DE_ATENDIMENTO_TEST[grupo_atendimento_os]
    elif mk == 1:
        instance = Mk(
            username=os.getenv('USERNAME_MK1'),
            password=os.getenv('PASSWORD_MK1'),
            url=os.getenv('URL_MK1'),
        )
        motivo_de_cancelamento  = MOTIVO_DE_CANCELAMENTO_MK01["Inadimplência"]
        valor_tipo_de_os = TIPO_DA_OS[tipo_da_os]
        valor_grupo_atendimento = GRUPO_DE_ATENDIMENTO_MK01[grupo_atendimento_os]
    elif mk == 3:
        instance = Mk(
            username=os.getenv('USERNAME_MK3'),
            password=os.getenv('PASSWORD_MK3'),
            url=os.getenv('URL_MK3'),
        )
        motivo_de_cancelamento  = MOTIVO_DE_CANCELAMENTO_MK03["Inadimplência"]
        valor_tipo_de_os = TIPO_DA_OS[tipo_da_os]
        valor_grupo_atendimento = GRUPO_DE_ATENDIMENTO_MK03[grupo_atendimento_os]

    else:
        logging.warning('Error na escolha do mk')

    financeiro = Financeiro()
    painel_do_cliente = PainelDoCliente()

    instance.login()

    instance.minimizeChat()

    # fechar tela de complete seu cadastro
    try:
        instance.iframeMain()
        instance.click('//div[@class="OptionClose"]')
    except:
        print("Sem tela de complete seu cadastro")
        
    # click na moeda financeiro
    instance.iframeCoin()
    instance.click(financeiro.xpath())

    # click aside Painel do cliente
    instance.iframeAsideCoin(financeiro)
    instance.click(painel_do_cliente.xpath())

    # click pesquisa avançada
    instance.iframePainel(financeiro, painel_do_cliente)
    instance.click('//*[@title="Clique para fazer uma pesquisa avançada de clientes ou fornecedores"]')

    # pesquisar por Código de cadastro
    instance.iframeForm()
    instance.click('//*[@class="HTMLComboBox"]/div[2]/div')
    instance.write('//input[@id="lookupSearchQuery"]', "C" + Keys.ENTER)
    instance.click('//option[@value="7"]')
    instance.write('//input[@title="Código do cliente."]', cod_pessoa)
    instance.click('//button[@title="Clique para efetivar sua pesquisa."]')

    # click no resultado de pesquisa avançada
    instance.iframeGrid(financeiro, painel_do_cliente)
    instance.dbclick(f'//div[text()={cod_pessoa}]')

    # click no resultado do click duplo no cadastro do cliente
    instance.iframeGridRes(financeiro, painel_do_cliente)
    instance.click(f'//div[text()={contrato}]')

    # criar multa em caso do contrato ter multa
    if incidencia_multa:

        # click no botão editar contrato
        instance.iframePainel(financeiro, painel_do_cliente)
        instance.click('//*[@title="Alterar contrato"]')

        # click no botão contas associadas
        instance.iframeForm()
        instance.click('//button[@title="Contas associadas ao contrato"]')

        # click inserir nova conta
        instance.click('//button[@title="Inserir nova conta no contrato."]')

        # criar multa
        instance.iframeFormRes()

        # descricao da multa
        instance.write('//*[@title="Descrição identificativa da conta."]', "Multa por rescisão contratual")

        # valor da multa
        instance.write('//*[@title="Valor do lançamento"]', valor_multa)

        # vencimento da multa
        instance.write('//*[@title="Data de vencimento da conta."]', vencimento_multa)

        # quantidade de parcelas
        instance.write('//*[@title="Número de parcela"]', 1)

        # plano de contas
        instance.click('//*[@title="Unidade de plano de contas referenciada para o lançamento"]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', f"{planos_contas.split()[0]}" + Keys.ENTER)
        instance.click(f'//option[@value="{planos_contas.split()[0]}"]')

        # próxima etapa da multa
        instance.click('//*[@title="Próxima etapa."]')

        # faturar ?
        instance.click('//div[@title="Deseja faturar agora estas contas?\nMarcando SIM, será criada uma fatura 1/1 para cada conta inserida."]/div/button')
        instance.click('//option[@value="S"]')

        # qual profile usar
        instance.click('//div[@title="Selecione a profile desejada"]/div/button')
        instance.write('//input[@id="lookupSearchQuery"]', "5155" + Keys.ENTER)
        instance.click('//option[@value="590"]')

        # marca check box
        instance.click('//input[@title="Marque essa opção para confirmar seu desejo de inserir a nova conta."]')

        # concluir multa
        instance.click('//button[@title="Clique para realizar a inserção"]')

        # fechar visualizar/Editar contrato
        instance.iframeMain()
        instance.click('//div[@class="OptionClose"]')

    # click no resultado do click duplo no cadastro do cliente
    instance.iframeGridRes(financeiro, painel_do_cliente)
    instance.click(f'//div[text()={contrato}]')

    # click cancelar contrato
    instance.iframePainel(financeiro, painel_do_cliente)
    instance.click('//*[@title="Cancelar contrato"]')

    # Motivo de cancelamento
    instance.iframeForm()
    instance.click('//div[@title="Selecione um motivo de cancelamento."]/div/button')
    instance.write('//input[@id="lookupSearchQuery"]', "Inadi" + Keys.ENTER)
    instance.click(f'//option[@value="{motivo_de_cancelamento}"]') 

    # detalhes do motivo de cancelamento
    instance.write('//textarea[@title="Informe detalhes do cancelamento do contrato."]', detalhes_cancelamento)

    # proxima etapa do cancelar contrato
    instance.click('//div[@class="HTMLTabContainer"]/div[2]/div[@class="next"]')

    # proxima etapa do cancelar contrato
    instance.click('//div[@class="HTMLTabContainer"]/div[3]/div[@class="next"]')
    
    # checkbox Abrir O.S de retirada de equipamentos
    instance.click('//*[@title="Marque esta opção, para que seja aberta uma O.S. de retirada de equipamentos para este cliente."]')

    # Tipo da O.S
    instance.click('//div[@title="Informa qual o tipo da Ordem de Serviço."]/div/button')
    instance.write('//input[@id="lookupSearchQuery"]', tipo_da_os + Keys.ENTER)
    instance.click(f'//option[@value="{valor_tipo_de_os}"]')

    # Grupo de atendimento
    instance.click('//div[@class="HTMLTabContainer"]/div[5]/div[7]/div[2]/div/button')
    instance.write('//input[@id="lookupSearchQuery"]', grupo_atendimento_os + Keys.ENTER)
    instance.click(f'//option[@value="{valor_grupo_atendimento}"]')

    # Defeito
    instance.click('//div[@title="Neste campo é informado o defeito associado a esta Ordem de Serviço."]/div/button')
    instance.write('//input[@id="lookupSearchQuery"]', "C" + Keys.ENTER)
    instance.click(f'//option[@value="{DEFEITO["Cancelamento contratual"]}"]')

    # Descrição da O.S.
    instance.write('//textarea[@title="Descreva as informações para a sua O.S."]', relato_do_problema)

    # proxima etapa do cancelar contrato
    instance.click('//div[@class="HTMLTabContainer"]/div[5]/div[@class="next"]')

    # click checkbox cancelar contrato
    instance.click('//div[@class="HTMLTabContainer"]/div[6]/div[12]/input[@type="checkbox"]')

    # Terminar cancelamento contrato
    instance.click('//button[@title="Clique para finalizar"]')

    # alert concluir cancelamento
    instance.include()

    time.sleep(10)
    instance.close()
