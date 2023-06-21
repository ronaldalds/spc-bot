import time
from driver.spc.spc_driver import Spc
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

SUCESS = 35
logging.addLevelName(SUCESS,'SUCESS')

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
    file_log = datetime.now().strftime("spc_%Y-%m-%d.log")
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(__file__), 'logs', file_log),
        encoding='utf-8',
        filemode='a',
        format='%(levelname)s - %(asctime)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.WARNING
        )
    
    print(f'cadastrando cpf:{cpf_cnpj}')
    
    try:
        spc = Spc(
            url=os.getenv('URL_SPC'),
            operation=os.getenv('OPERATION_SPC'),
            password=os.getenv('PASSWORD_SPC'),
            secret=os.getenv('SECRET_KEY_SPC'),
            )
        
        try:
            # login no sistema spc
            spc.login()
        except:
            logging.error('Failed to login')
            spc.close()
            return

        # click bottun Inclusão
        spc.click('//*[text()="Inclusão/Exclusão"]')

        # click menu principal
        spc.click('//a[@class="menu-principal"]')

        # click sub-menu
        spc.click('//a[@class="sub-menu"]')

        # click novo
        spc.click('//*[@name="SPC (INC/EXC) - Novo"]')

        # cpf
        spc.write('//*[@id="consumidorPessoaFisica.cpf"]', cpf_cnpj + Keys.TAB)
        time.sleep(5)

        # cpf não localizado
        if spc.text('//*[@id="consumidorPessoaFisica.nome"]') == 'CADASTRO NAO LOCALIZADO':
            msgCadastro = f'CPF: {cpf_cnpj} - cadastro nao localizado'
            logging.warning(msgCadastro)
            spc.close()
            return

        # data de nascimento nao cadastrada
        if spc.text('//*[@id="consumidorPessoaFisica.dataNascimento"]') == '':
            try:
                # escrever data de nasicmento
                spc.write('//*[@id="consumidorPessoaFisica.dataNascimento"]', data_nascimento + Keys.TAB)
            except:
                logging.error(f'Error na data {data_nascimento}')
                spc.close()
                return

        # ddd
        spc.write('//*[@id="consumidorPessoaFisica.telefones0.numeroDDD"]', ddd)

        # celular
        spc.write('//*[@id="consumidorPessoaFisica.telefones0.numero"]', celular)

        # cep
        try:
            spc.write('//input[@id="consumidorPessoaFisica.enderecos0.cep"]', cep + Keys.TAB)
        except:
            logging.error(f'Error no {cep}')
            spc.close()
            return

        # logradouro
        spc.write('//*[@name="consumidorPessoaFisica.enderecos[0].logradouro"]', logradouro)

        # numero
        spc.write('//*[@id="consumidorPessoaFisica.enderecos0.numero"]', numero)

        # complemento
        spc.write('//*[@id="consumidorPessoaFisica.enderecos0.complemento"]', complemento)

        # bairro
        spc.write('//*[@id="consumidorPessoaFisica.enderecos0.bairro"]', bairro)

        # data vencimento
        try:
            spc.write('//*[@id="dataVencimento"]', data_vencimento + Keys.TAB)
        except:
            logging.error(f'Error na data {data_vencimento}')
            spc.close()
            return

        # data da compra
        try:
            spc.write('//*[@id="dataCompra"]', data_compra + Keys.TAB)
        except:
            logging.error(f'Error na data {data_compra}')
            spc.close()
            return

        # código do cliente
        spc.write('//*[@id="numeroContrato"]', cod_cliente + Keys.TAB)

        # valor do debito
        spc.write('//*[@id="valorDebito"]', valor_debito + Keys.TAB)

        # concluir inclusão do cliente
        spc.click('//*[@id="idButtonNotificacaoDebitoFisica"]')
        spc.include()

        logging.log(SUCESS, f'CPF: {cpf_cnpj} - Cadastrado com sucesso')
        time.sleep(10)
        spc.close()

    except:
        logging.error(f'CPF: {cpf_cnpj} - Erro no cadastro do cliente')
        