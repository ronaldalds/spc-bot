import time
from driver.spc.spc_driver import Spc
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

def include(
        cpf_cnpj,
        data_nascimento,
        ddd,
        celular,
        cep,
        logradouro,
        numero,
        complemento,
        bairro,
        data_vencimento,
        data_compra,
        cod_cliente,
        valor_debito,
        ):
    
    # configuração logs
    SUCESS = 35
    logging.addLevelName(SUCESS,'SUCESS')
    file_log_spc = datetime.now().strftime("%Y-%m-%d.log")
    logging.basicConfig(
        level=logging.WARNING,
        filename=os.path.join(os.path.dirname(__file__), 'logs', file_log_spc),
        format='%(levelname)s - %(name)s - %(asctime)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        encoding='utf-8',
        filemode='a'
        )
    
    logger_spc = logging.getLogger("spc")
    # formatter = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
    # file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'logs', file_log_spc))
    # file_handler.setFormatter(formatter)
    # logger_spc.addHandler(file_handler)
    prefixo_log_spc = f'Cpf:{cpf_cnpj} código:{cod_cliente} valor debito:{valor_debito}'

    print(f'Incluindo spc cpf:{cpf_cnpj}')
    
    instance = Spc(
        url=os.getenv('URL_SPC'),
        operation=os.getenv('OPERATION_SPC'),
        password=os.getenv('PASSWORD_SPC'),
        secret=os.getenv('SECRET_KEY_SPC'),
        )
    
    # login no sistema spc
    try:
        instance.login()
    except:
        logger_spc.error(f'{prefixo_log_spc} - Failed to login')
        instance.close()
        return

    # click bottun Inclusão
    try:
        instance.click('//*[text()="Inclusão/Exclusão"]')
    except:
        logger_spc.error(f'{prefixo_log_spc}  - click bottun Inclusão')
        instance.close()
        return

    # click menu principal
    try:
        instance.click('//a[@class="menu-principal"]')
    except:
        logger_spc.error(f'{prefixo_log_spc}  - click menu principal')
        instance.close()
        return

    # click sub-menu
    try:
        instance.click('//a[@class="sub-menu"]')
    except:
        logger_spc.error(f'{prefixo_log_spc}  - click sub-menu')
        instance.close()
        return

    # click novo
    try:
        instance.click('//*[@name="SPC (INC/EXC) - Novo"]')
    except:
        logger_spc.error(f'{prefixo_log_spc}  - click novo')
        instance.close()
        return

    # escrever cpf
    try:
        instance.write('//*[@id="consumidorPessoaFisica.cpf"]', cpf_cnpj + Keys.TAB)
        time.sleep(5)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever cpf')
        instance.close()
        return

    # cpf não localizado
    if instance.text('//*[@id="consumidorPessoaFisica.nome"]') == 'CADASTRO NAO LOCALIZADO':
        logger_spc.error(f'{prefixo_log_spc}  - cpf não localizado')
        instance.close()
        return

    # data de nascimento nao cadastrada
    if instance.text('//*[@id="consumidorPessoaFisica.dataNascimento"]') == '':
        # escrever data de nasicmento
        try:
            instance.write('//*[@id="consumidorPessoaFisica.dataNascimento"]', data_nascimento + Keys.TAB)
        except:
            logger_spc.error(f'{prefixo_log_spc}  - escrever data de nasicmento')
            instance.close()
            return

    # escrever ddd
    try:
        instance.write('//*[@id="consumidorPessoaFisica.telefones0.numeroDDD"]', ddd)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever ddd')
        instance.close()
        return

    # escrever celular
    try:
        instance.write('//*[@id="consumidorPessoaFisica.telefones0.numero"]', celular)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever celular')
        instance.close()
        return

    # escrever cep
    try:
        instance.write('//input[@id="consumidorPessoaFisica.enderecos0.cep"]', cep + Keys.TAB)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever cep')
        instance.close()
        return

    # escrever logradouro
    try:
        instance.write('//*[@name="consumidorPessoaFisica.enderecos[0].logradouro"]', logradouro)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever logradouro')
        instance.close()
        return

    # escrever número
    try:
        instance.write('//*[@id="consumidorPessoaFisica.enderecos0.numero"]', numero)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever número')
        instance.close()
        return

    # escrever complemento
    try:
        instance.write('//*[@id="consumidorPessoaFisica.enderecos0.complemento"]', complemento)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever complemento')
        instance.close()
        return

    # escrever bairro
    try:
        instance.write('//*[@id="consumidorPessoaFisica.enderecos0.bairro"]', bairro)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever bairro')
        instance.close()
        return

    # escrever data vencimento
    try:
        instance.write('//*[@id="dataVencimento"]', data_vencimento + Keys.TAB)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever data vencimento')
        instance.close()
        return

    # escrever data da compra
    try:
        instance.write('//*[@id="dataCompra"]', data_compra + Keys.TAB)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever data da compra')
        instance.close()
        return

    # escrever código do cliente
    try:
        instance.write('//*[@id="numeroContrato"]', cod_cliente + Keys.TAB)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever código do cliente')
        instance.close()
        return

    # escrever valor do debito
    try:
        instance.write('//*[@id="valorDebito"]', valor_debito)
    except:
        logger_spc.error(f'{prefixo_log_spc}  - escrever valor do debito')
        instance.close()
        return

    # click botão de incluir cliente
    try:
        instance.click('//*[@id="idButtonNotificacaoDebitoFisica"]')
        instance.click('//*[@id="idButtonNotificacaoRegistroInteligente"]')
    except:
        logger_spc.error(f'{prefixo_log_spc}  - click botão de incluir cliente')
        instance.close()
        return

    # alert concluir incluir spc 
    instance.include()

    # log incluir spc conluído
    logger_spc.log(SUCESS, f'{prefixo_log_spc}  - incluir spc conluído')

    time.sleep(10)
    instance.close()
    