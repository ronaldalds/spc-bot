import os
import time
from datetime import datetime
from dotenv import load_dotenv
from Src.Api.spc.spc_driver import Spc
from selenium.webdriver.common.keys import Keys

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
    
    hora = datetime.now()
    print(f'Iniciou SPC {hora.strftime("%d/%m/%Y %H:%M")} CPF/CNPJ:{cpf_cnpj} Cod Cliente:{cod_cliente} Débito:{valor_debito}')
    error = f"\033[91mERROR\033[0m;SPC;{hora.strftime('%d/%m/%Y %H:%M')}"
    warning = f"\033[93mWARNING\033[0m;SPC;{hora.strftime('%d/%m/%Y %H:%M')}"
    sucess = f"\033[92mSUCESS\033[0m;SPC;{hora.strftime('%d/%m/%Y %H:%M')}"

    prefixo_log_spc = f'CPF/CNPJ:{cpf_cnpj} Cod Cliente:{cod_cliente} Débito:{valor_debito}'

    # criar instância do spc
    try:
        instance = Spc(
            url=os.getenv('URL_SPC'),
            operation=os.getenv('OPERATION_SPC'),
            password=os.getenv('PASSWORD_SPC'),
            secret=os.getenv('SECRET_KEY_SPC'),
            )
    except:
        print(f'{error};{prefixo_log_spc};Não foi possível criar instancia do SPC...')
        return f'{error};{prefixo_log_spc};Não foi possível criar instancia do SPC...'
    
    # login no sistema spc
    try:
        instance.login()
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};Failed to login')
        return f'{error};{prefixo_log_spc};Failed to login'

    # click bottun Inclusão
    try:
        instance.click('//*[text()="Inclusão/Exclusão"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};click bottun Inclusão')
        return f'{error};{prefixo_log_spc};click bottun Inclusão'

    # click menu principal
    try:
        instance.click('//a[@class="menu-principal"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};click menu principal')
        return f'{error};{prefixo_log_spc};click menu principal'

    # click sub-menu
    try:
        instance.click('//a[@class="sub-menu"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};click sub-menu')
        return f'{error};{prefixo_log_spc};click sub-menu'

    # click novo
    try:
        instance.click('//*[@name="SPC (INC/EXC) - Novo"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};click novo')
        return f'{error};{prefixo_log_spc};click novo'

    # escrever cpf
    try:
        instance.write('//*[@id="consumidorPessoaFisica.cpf"]', cpf_cnpj + Keys.TAB)
        time.sleep(5)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever cpf')
        return f'{error};{prefixo_log_spc};escrever cpf'

    # cpf não localizado
    if instance.text('//*[@id="consumidorPessoaFisica.nome"]') == 'CADASTRO NAO LOCALIZADO':
        instance.close()
        print(f'{error};{prefixo_log_spc};cpf não localizado')
        return f'{error};{prefixo_log_spc};cpf não localizado'

    # data de nascimento nao cadastrada
    if instance.text('//*[@id="consumidorPessoaFisica.dataNascimento"]') == '':
        # escrever data de nasicmento
        try:
            instance.write('//*[@id="consumidorPessoaFisica.dataNascimento"]', data_nascimento + Keys.TAB)
        except:
            instance.close()
            print(f'{error};{prefixo_log_spc};escrever data de nasicmento')
            return f'{error};{prefixo_log_spc};escrever data de nasicmento'

    # escrever ddd
    try:
        instance.write('//*[@id="consumidorPessoaFisica.telefones0.numeroDDD"]', ddd)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever ddd')
        return f'{error};{prefixo_log_spc};escrever ddd'

    # escrever celular
    try:
        instance.write('//*[@id="consumidorPessoaFisica.telefones0.numero"]', celular)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever celular')
        return f'{error};{prefixo_log_spc};escrever celular'

    # escrever cep
    try:
        instance.write('//input[@id="consumidorPessoaFisica.enderecos0.cep"]', cep + Keys.TAB)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever cep')
        return f'{error};{prefixo_log_spc};escrever cep'

    # escrever logradouro
    try:
        instance.write('//*[@name="consumidorPessoaFisica.enderecos[0].logradouro"]', logradouro)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever logradouro')
        return

    # escrever número
    try:
        instance.write('//*[@id="consumidorPessoaFisica.enderecos0.numero"]', numero)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever número')
        return f'{error};{prefixo_log_spc};escrever número'

    # escrever complemento
    try:
        instance.write('//*[@id="consumidorPessoaFisica.enderecos0.complemento"]', complemento)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever complemento')
        return f'{error};{prefixo_log_spc};escrever complemento'

    # escrever bairro
    try:
        instance.write('//*[@id="consumidorPessoaFisica.enderecos0.bairro"]', bairro)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever bairro')
        return f'{error};{prefixo_log_spc};escrever bairro'

    # escrever data vencimento
    try:
        instance.write('//*[@id="dataVencimento"]', data_vencimento + Keys.TAB)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever data vencimento')
        return

    # escrever data da compra
    try:
        instance.write('//*[@id="dataCompra"]', data_compra + Keys.TAB)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever data da compra')
        return f'{error};{prefixo_log_spc};escrever data da compra'

    # escrever código do cliente
    try:
        instance.write('//*[@id="numeroContrato"]', cod_cliente + Keys.TAB)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever código do cliente')
        return f'{error};{prefixo_log_spc};escrever código do cliente'

    # escrever valor do debito
    try:
        instance.write('//*[@id="valorDebito"]', valor_debito + Keys.TAB)
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};escrever valor do debito')
        return f'{error};{prefixo_log_spc};escrever valor do debito'

    # click botão de incluir cliente
    try:
        instance.click('//*[@value="INCLUIR E ENVIAR NOTIF. FÍSICA"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};click botão de incluir cliente')
        return f'{error};{prefixo_log_spc};click botão de incluir cliente'

    # alert concluir incluir spc 
    try:
        instance.include()
    except:
        instance.close()
        print(f'{error};{prefixo_log_spc};alert para concluir')
        return f'{error};{prefixo_log_spc};alert para concluir'

    time.sleep(5)
    instance.close()
    print(f'{sucess};{prefixo_log_spc};incluir spc conluído')
    return f'{sucess};{prefixo_log_spc};incluir spc conluído'
    