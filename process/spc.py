import time
from driver.spc.spc_driver import Spc
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

file_log = datetime.now().strftime("spc_include_%d_%m_%Y.log")
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
        valor_debito
):
    print(
        f'cadastrando {cpf_cnpj}')
    try:
        spc = Spc(
            url=os.getenv('URL_SPC'),
            operation=os.getenv('OPERATION_SPC'),
            password=os.getenv('PASSWORD_SPC'),
            secret=os.getenv('SECRET_KEY_SPC')
        )

        spc.login()
        spc.click('//*[text()="Inclusão/Exclusão"]')
        spc.click('//a[@class="menu-principal"]')
        spc.click('//a[@class="sub-menu"]')
        spc.click('//*[@name="SPC (INC/EXC) - Novo"]')
        spc.write('//*[@id="consumidorPessoaFisica.cpf"]', cpf_cnpj + Keys.TAB)
        time.sleep(5)
        if spc.text('//*[@id="consumidorPessoaFisica.nome"]') == 'CADASTRO NAO LOCALIZADO':
            msgCadastro = f'CPF: {cpf_cnpj} - cadastro nao localizado'
            logging.warning(msgCadastro)
            spc.close()
            return

        if spc.text('//*[@id="consumidorPessoaFisica.dataNascimento"]') == '':
            spc.write(
                '//*[@id="consumidorPessoaFisica.dataNascimento"]', data_nascimento + Keys.TAB)
        spc.write(
            '//*[@id="consumidorPessoaFisica.telefones0.numeroDDD"]', ddd)
        spc.write(
            '//*[@id="consumidorPessoaFisica.telefones0.numero"]', celular)
        spc.write(
            '//input[@id="consumidorPessoaFisica.enderecos0.cep"]', cep + Keys.TAB)
        spc.write(
            '//*[@name="consumidorPessoaFisica.enderecos[0].logradouro"]', logradouro)
        spc.write(
            '//*[@id="consumidorPessoaFisica.enderecos0.numero"]', numero)
        spc.write(
            '//*[@id="consumidorPessoaFisica.enderecos0.complemento"]', complemento)
        spc.write(
            '//*[@id="consumidorPessoaFisica.enderecos0.bairro"]', bairro)
        spc.write('//*[@id="dataVencimento"]', data_vencimento + Keys.TAB)
        spc.write('//*[@id="dataCompra"]', data_compra + Keys.TAB)
        spc.write('//*[@id="numeroContrato"]', cod_cliente + Keys.TAB)
        spc.write('//*[@id="valorDebito"]', valor_debito + Keys.TAB)
        spc.include()
        msgSucess = f'CPF: {cpf_cnpj} - Cadastrado com sucesso'
        logging.log(SUCESS, msgSucess)
        print(msgSucess)
        spc.close()
    except:
        msgErro = f'CPF: {cpf_cnpj} - Erro no cadastro do cliente'
        logging.error(msgErro)