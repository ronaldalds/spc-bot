import time
from driver.avin.avin_driver import Avin
from dotenv import load_dotenv
import os
import pandas
import csv
import logging
import codecs
from datetime import datetime, timedelta

load_dotenv()

def ler_arquivo_csv(caminho_arquivo, data_atual):
    caminho_arquivo = caminho_arquivo.replace(f'{os.path.dirname(__file__)}/downloads/', '')
    result = []
    avisos = pandas.read_csv(os.path.join(os.path.dirname(__file__), 'downloads', caminho_arquivo), encoding="ISO-8859-1", sep=';')
    avisos.drop(columns=['#', 'Data tratamento', 'Data GPS', 'Motorista', 'Atendente'], inplace=True)

    # avisos['Ocorrência'] = avisos['Ocorrência'].apply(lambda data_str: data_str[:-3])

    # Diferenca = list()

    # for _, row in avisos.iterrows():
    #     data_aviso = row[0]
    #     diferenca = datetime.strptime(data_atual, "%d/%m/%Y %H:%M") - datetime.strptime(data_aviso,"%d/%m/%Y %H:%M")
    #     Diferenca.append(diferenca.seconds)
    
    # avisos.insert(2, "segundos", Diferenca, True)
    # avisos = avisos.loc[avisos["segundos"] <= 600]

    Veiculos = list(set(avisos['Veículo'].to_list()))

    for veiculo in Veiculos:
        txt = '🚧🚨 VELOCIDADE MÁXIMA EXCEDIDA 🚨🚧\n\n'
        ocorrencias = avisos.query(f"Veículo == '{veiculo}'")
        txt += '🚗 ' + veiculo + '\n\n'

        for ocor in ocorrencias['Ocorrência']:
            txt += '⏰ ' + ocor + '\n'

        result.append(txt)
    # linhas = []

    # with codecs.open(os.path.join(os.path.dirname(__file__), 'downloads', caminho_arquivo), 'r', encoding='utf-8', errors='replace') as arquivo_csv:
    #     leitor_csv = csv.reader(arquivo_csv)
    #     for linha in leitor_csv:
    #         linhas.append(linha)
    
    os.remove(os.path.join(os.path.dirname(__file__), 'downloads', caminho_arquivo))
    
    # if len(linhas) == 0:
    #     return False

    # return linhas
    return result

def x9(data: datetime):
    
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
    duracao = timedelta(minutes=31)
    data_inicial = (data - duracao).strftime('%d/%m/%Y')
    hora_inicial = (data - duracao).hour
    minuto_inicial = (data - duracao).minute
    data_final = data.strftime('%d/%m/%Y')
    hora_final = data.hour
    minuto_final = data.minute
    # print(data_inicial)
    # print(hora_inicial)
    # print(minuto_inicial)
    # print(data_final)
    # print(hora_final)
    # print(minuto_final)
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
        instance.write('//div[@id="horaInicial_chosen"]/div/div/input', str(hora_inicial).zfill(2))
        instance.click(f'//div[@id="horaInicial_chosen"]/div/ul/li[@data-option-array-index={hora_inicial}]')
    except:
        logger_x9.error('Selecionar Hora Inicial...')
        instance.close()
        return

    # Minuto Inicial
    try:
        instance.click('//div[@id="minutoInicial_chosen"]/a')
        instance.write('//div[@id="minutoInicial_chosen"]/div/div/input', str(minuto_inicial).zfill(2))
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
        instance.write('//div[@id="horaFinal_chosen"]/div/div/input', str(hora_final).zfill(2))
        instance.click(f'//div[@id="horaFinal_chosen"]/div/ul/li[@data-option-array-index={hora_final}]')
    except:
        logger_x9.error('Selecionar Hora Final...')
        instance.close()
        return

    # Minuto Inicial
    try:
        instance.click('//div[@id="minutoFinal_chosen"]/a')
        instance.write('//div[@id="minutoFinal_chosen"]/div/div/input', str(minuto_final).zfill(2))
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
        instance.click('//div[@id="gerar_relatorio"]')
    except:
        logger_x9.error('Gerar Relatório...')
        instance.close()
        return

    # Exportar
    try:
        instance.click('//div[@id="export-dropdown"]')
    except:
        logger_x9.log(SUCESS, 'Sem Ocorrência...')
        instance.close()
        return

    # Exportar CSV
    try:
        instance.click('//a[@class="csv-button"]')
        time.sleep(5) # esperar para terminar download
    except:
        logger_x9.error('Exportar csv...')
        instance.close()
        return

    # file CSV
    try:
        cod_file = instance.download('//a[@class="csv-button"]').split('selecionado(s)-')[1]
    except:
        logger_x9.error('file csv...')
        instance.close()
        return

    # caminho do diretório de downloads
    diretorio_download = os.path.join(os.path.dirname(__file__), 'downloads')

    # lista todos os arquivos dentro do diretório
    arquivos = os.listdir(diretorio_download)

    # verifica se existe arquivos no diretório de downloads
    if arquivos:
        caminho_arquivo = None
        for arquivo in arquivos:
            if cod_file in arquivo:  # Substitua pelo formato correto do nome do arquivo
                caminho_arquivo = arquivo
                break
        
        result_ocor = ler_arquivo_csv(caminho_arquivo, data) # faz leitura do arquivos csv em caso de existir alguma ocorrência
    
    # log x9 concluído
    logger_x9.log(SUCESS, 'x9 concluído')

    time.sleep(5)
    instance.close()

    return result_ocor