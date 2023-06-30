import time
from driver.avin.avin_driver import Avin
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv()

def x9(
        data_inicial,
        hora_inicial,
        minuto_inicial,
        data_final,
        hora_final,
        minuto_final
        ):
    
    # configuração logs
    SUCESS = 35
    logging.addLevelName(SUCESS,'SUCESS')
    file_log_x9 = datetime.now().strftime("%Y-%m-%d.log")
    logging.basicConfig(
        level=logging.WARNING,
        filename=os.path.join(os.path.dirname(__file__), 'logs', file_log_x9),
        format='%(levelname)s - %(name)s - %(asctime)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        encoding='utf-8',
        filemode='a'
        )
    logger_x9 = logging.getLogger("x9")
    
    try:
        instance = Avin(
            username=os.getenv('USERNAME_AVIN'),
            password=os.getenv('PASSWORD_AVIN'),
            url=os.getenv('URL_AVIN'),
            )
    except:
        logger_x9.error('Não foi possível criar instancia do avin...')

    try:
        instance.login()
    except:
        logger_x9.error('login avin...')
        instance.close()
        return

    try:
        instance.click('//a[@class="pull-left sidebar-toggle ft-menu-toggle"]')
    except:
        logger_x9.error('Abrir aside...')
        instance.close()
        return

    try:
        instance.click('//span[text()="Relatórios"]')
    except:
        logger_x9.error('Click Relatórios...')
        instance.close()
        return

    try:
        instance.click('//a[@href="https://gpsa.avinrastreamento.com.br/relatorios/alertas_controller"]')
    except:
        logger_x9.error('Click Alertas...')
        instance.close()
        return

    # Seleciona Cliente
    try:
        instance.click('//div[@id="idCliente_chosen"]/a')
        instance.click(f'//div[@id="idCliente_chosen"]/div/ul/li[@data-option-array-index="1"]')
    except:
        logger_x9.error('Selecionar Cliente...')
        instance.close()
        return

    # Data Inicial
    try:
        instance.write('//input[@id="dataInicial"]', data_inicial)
    except:
        logger_x9.error('Data Inicial...')
        instance.close()
        return

    # Hora Inicial
    try:
        instance.click('//div[@id="horaInicial_chosen"]/a')
        instance.write('//div[@id="horaInicial_chosen"]/div/div/input', hora_inicial)
        instance.click(f'//div[@id="horaInicial_chosen"]/div/ul/li[@data-option-array-index={hora_inicial}]')
    except:
        logger_x9.error('Selecionar Hora Inicial...')
        instance.close()
        return

    # Minuto Inicial
    try:
        instance.click('//div[@id="minutoInicial_chosen"]/a')
        instance.write('//div[@id="minutoInicial_chosen"]/div/div/input', minuto_inicial)
        instance.click(f'//div[@id="minutoInicial_chosen"]/div/ul/li[@data-option-array-index={minuto_inicial}]')
    except:
        logger_x9.error('Selecionar Minuto Inicial...')
        instance.close()
        return

    # Data Final
    try:
        instance.write('//input[@id="dataFinal"]', data_final)
    except:
        logger_x9.error('Data Final...')
        instance.close()
        return

    # Hora Final
    try:
        instance.click('//div[@id="horaFinal_chosen"]/a')
        instance.write('//div[@id="horaFinal_chosen"]/div/div/input', hora_final)
        instance.click(f'//div[@id="horaFinal_chosen"]/div/ul/li[@data-option-array-index={hora_final}]')
    except:
        logger_x9.error('Selecionar Hora Final...')
        instance.close()
        return

    # Minuto Inicial
    try:
        instance.click('//div[@id="minutoFinal_chosen"]/a')
        instance.write('//div[@id="minutoFinal_chosen"]/div/div/input', minuto_final)
        instance.click(f'//div[@id="minutoFinal_chosen"]/div/ul/li[@data-option-array-index={minuto_final}]')
    except:
        logger_x9.error('Selecionar Minuto Final...')
        instance.close()
        return

    # Velocidade Máxima Excedida
    try:
        instance.click('//div[@id="tipoAlerta_chosen"]/a')
        instance.write('//div[@id="tipoAlerta_chosen"]/div/div/input', "Velocidade Máxima Excedida")
        instance.click(f'//div[@id="tipoAlerta_chosen"]/div/ul/li[@data-option-array-index="91"]')
    except:
        logger_x9.error('Selecionar Velocidade Máxima Excedida...')
        instance.close()
        return

    # Alertas Todos
    try:
        instance.click('//input[@name="statusDosAlertas" and @value="todos"]')
    except:
        logger_x9.error('Selecionar Todos Alertas...')
        instance.close()
        return

    # Gerar Relatório
    try:
        instance.click('//div[@id="gerar_relatorio""]')
    except:
        logger_x9.error('Gerar Relatório...')
        instance.close()
        return

    # Exportar
    try:
        instance.click('//div[@id="export-dropdown"]')
    except:
        logger_x9.error('Sem Ocorrência...')
        instance.close()
        return

    # Exportar CSV
    try:
        instance.click('//a[@class="csv-button"]')
    except:
        logger_x9.error('Exportar csv...')
        instance.close()
        return

    # file CSV
    try:
        print(instance.download('//a[@class="csv-button"]'))
    except:
        logger_x9.error('file csv...')
        instance.close()
        return

    # log x9 concluído
    logger_x9.log(SUCESS, 'x9 concluído')
    print(f"Processo X9 concluído.")

    time.sleep(10)
    instance.close()

    return