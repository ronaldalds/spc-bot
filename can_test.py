from process.x9 import x9
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from pyrogram import Client
from api.avin.api_avin import APIavin
from urllib import request, parse
from collections import Counter
load_dotenv()

avin = APIavin()
ajuste_gmt = timedelta(hours=3)
data = datetime(day=8, month=7, year=2023, hour=00, minute=00)
# data = datetime.now()
duracao = timedelta(minutes=1440)
data_inicial = (data - duracao)
data_final = data
print(data_inicial)
print(data_final)
print(data_inicial + ajuste_gmt)
print(data_final + ajuste_gmt)
print(int(data_inicial.timestamp()))
print(int(data_final.timestamp()))
print(int(data_final.timestamp()) - int(data_inicial.timestamp()))

# dados = avin.alerts_period(inicial=int(data_inicial.timestamp()), final=int(data_final.timestamp()))
print(x9(data, 1440))
# for i in dados:
#     placa = avin.veiculo_id(i['ras_eal_id_veiculo'])[0]['ras_vei_tag_identificacao']
#     veiculo = avin.veiculo_id(i['ras_eal_id_veiculo'])[0]['ras_vei_veiculo']
#     i['ras_eal_id_veiculo'] = f"{veiculo} - {placa}"
# lista_dicionarios = [
#     {'chave': 'valor1', 'outro': 'outro1'},
#     {'chave': 'valor2', 'outro': 'outro2'},
#     {'chave': 'valor3', 'outro': 'outro3'},
#     {'chave': 'valor1', 'outro': 'outro4'},
#     {'chave': 'valor2', 'outro': 'outro5'},
#     {'chave': 'valor3', 'outro': 'outro6'},
#     {'chave': 'valor4', 'outro': 'outro7'},
# ]
# if dados:
#     contador = Counter(d['placa'] for d in dados)
#     print(contador)

#     for i in contador:
#         resultado = list(filter(lambda d: d['placa'] == i, dados))
#         print(resultado)



# if dados:
#     for i in dados:
#         print(i)
# print(dados)
# url = "https://gpsa.avinrastreamento.com.br/token/Api_ftk4"
# url = "https://ws.fulltrack2.com/authorize/client"
# data = {
#     'ras_usu_login': 'bot.sistema',
#     'ras_usu_senha': 'botonline123',
#     # Adicione outros parâmetros conforme necessário
# }

# data_encoded = parse.urlencode(data).encode('utf-8')
# req = request.Request(url, data=data_encoded, method='POST')
# response = request.urlopen(req)
# data = response.read()
# text = data.decode('utf-8')
# print(data)
# print(text)
# app = Client(
#     name=os.getenv("BOT_NAME_TELEGRAM"), 
#     api_hash=os.getenv("API_HASH_TELEGRAM"),
#     api_id=os.getenv("API_ID_TELEGRAM"),
#     bot_token=os.getenv("BOT_TOKEN_TELEGRAM")
#     )
# grupo_transport = int(os.getenv('CHAT_ID_GROUP_TEST'))
# print(type(-1001550273372))
# print(type(int(os.getenv('CHAT_ID_GROUP_TEST'))))
# time = timedelta(minutes=31)
# data_inicial = (datetime.now() - time).strftime('%d/%m/%Y')
# hora_inicial = (datetime.now() - time).hour
# minuto_inicial = (datetime.now() - time).minute
# data_final = datetime.now().strftime('%d/%m/%Y')
# hora_final = datetime.now().hour
# minuto_final = datetime.now().minute

# print(data_inicial)
# print(hora_inicial)
# print(minuto_inicial)
# print(data_final)
# print(hora_final)
# print(minuto_final)
# test = x9(datetime.now())
# app.start()
# app.send_message(chat_id=grupo_transport, text="asdfasrtwqr")
# app.stop()
# test = x9(datetime(day=12, month=6, year=2023, hour=8, minute=10))
# for ocorrencia in test:
    # app.start()
    # enviar ocorrências
    # app.send_message(grupo_transport, ocorrencia)
    # app.stop()
# print(test)
# if test:
#     for i in test:
#         print(i)
        
# data_inicial = "11/06/2023"
# hora_inicial = "09"
# minuto_inicial = "30"
# data_final = "29/06/2023"
# hora_final = "11"
# minuto_final = "30"
# from driver.formatador import formatar_documento
# import copy
# from driver.spc.spc_driver import Spc
# import os
# from dotenv import load_dotenv

# load_dotenv()
# import os

# Obter a lista de arquivos na pasta /tmp
# arquivos_temporarios = os.listdir('/tmp')

# Excluir cada arquivo temporário na lista
# for arquivo_temporario in arquivos_temporarios:
#     caminho_arquivo = os.path.join('/tmp', arquivo_temporario)
#     os.remove(caminho_arquivo)
# instance = Spc(
#         url=os.getenv('URL_SPC'),
#         operation=os.getenv('OPERATION_SPC'),
#         password=os.getenv('PASSWORD_SPC'),
#         secret=os.getenv('SECRET_KEY_SPC'),
#         )

# instance.close()

# from selenium import webdriver

# Lista para armazenar as instâncias do driver
# drivers = []

# Abrir e armazenar instâncias do driver
# drivers.append(webdriver.Chrome())
# drivers.append(webdriver.Firefox())
# Adicione outras instâncias do driver, se necessário

# Encerrar todas as instâncias do driver
# for driver in drivers:
#     driver.quit()
# original_dict = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}}

# # Criando uma cópia usando o método copy()
# copia_shallow = original_dict.copy()

# # Criando uma cópia usando o método deepcopy()
# copia_deep = copy.deepcopy(original_dict)

# # Modificando os valores nas cópias
# copia_shallow['a'].append(4)
# copia_shallow['b']['x'] = 100

# copia_deep['a'].append(4)
# copia_deep['b']['x'] = 100

# # Imprimindo os dicionários
# print("Original:", original_dict)
# print("Cópia Shallow:", copia_shallow)
# print("Cópia Deep:", copia_deep)

# cancelamento(
#         mk = "test",
#         cod_pessoa = "152628",
#         contrato = "189726",
#         detalhes_cancelamento = """Cancelamento em razão de inadimplência superior a 75 dias, em conformidade com os artigos 90 a 100 da resolução nº 632/2014 da Anatel.
#         MAC: 00:E0:4C:CF:95:8B | Serial ONU: ITBS:E8A2D273 | Caixa: ARD AC.5.3.13 | Porta: 1 |
#         Multa: R$ 0,00""",
#         tipo_da_os = "Cancelamento - Fibra",
#         grupo_atendimento_os = "ARARENDÁ",
#         relato_do_problema = """Cancelamento em razão de inadimplência superior a 75 dias, em conformidade com os artigos 90 a 100 da resolução nº 632/2014 da Anatel

#         Observação1: Multa por quebra de contrato de R$ 0,00. Para negociar seu débito, basta entrar em contato pelo 0800-088-1111
#         Observação2: MAC - 00:E0:4C:CF:95:8B | Serial ONU - ITBS:E8A2D273 | Caixa - ARD AC.5.3.13 | Porta - 1
#         Observação3: Encerramento da OS de recolhimento de equipamentos deste contrato = Retirada Concluída""",
#         incidencia_multa = True,
#         valor_multa = '100,75',
#         vencimento_multa = '10062023',
#         planos_contas = "01.02.07 Cliente - Pessoa Física"
#     )
# print(formatar_documento("884.316.142-34 cod: 215082"))
# lojas_mk3 = {
#     "LOJA CASTANHAL": 18,
#     "LOJA VIGIA": 5,
#     "LOJA TERRA ALTA": 5,
#     "LOJA ICOARACI": 18,
#     "LOJA MARITUBA": 20,
#     "LOJA VILA DOS CABANOS": 10,
#     "LOJA BARCARENA": 5,
#     "LOJA MAGUARI": 5,
#     "LOJA ABAETETUBA": 15,
#     "LOJA TUCURUI": 10,
#     "LOJA TAILÂNDIA": 10,
#     "LOJA MOJU": 8,
#     "LOJA MOCAJUBA": 5,
#     "LOJA BAIÃO": 5
# }
# a = "LOJA BAIÃ"
# print(a in lojas_mk3.keys())
# print(lojas_mk3[a] - 1)

# def contar_e_deletar_ocorrencias(dicionario, lista):
#     lista_resultante = []
#     ocorrencias_dict = {chave: 0 for chave in dicionario}
#     print(ocorrencias_dict)
#     for item in lista:
#         chave = item[1] # posicao da tupla onde esta o que voce quer contar a ocorrencia
#         if chave in dicionario:
#             valor_limite = dicionario[chave]
#             if ocorrencias_dict[chave] < valor_limite:
#                 lista_resultante.append(item)
#                 ocorrencias_dict[chave] += 1
#         else:
#             lista_resultante.append(item)

#     return lista_resultante

# # Exemplo de uso
# meu_dicionario = {'a': 1, 'b': 1, 'c': 1}
# minha_lista = [('valor1', 'a'), ('valor2', 'b'), ('valor3', 'c'), ('valor4', 'a'), ('valor5', 'a'), ('valor6', 'c'), ('valor7', 'c'), ('valor8', 'c'), ('valor9', 'd'), ('valor10', 'e'), ('valor11', 'e')]

# minha_lista_resultante = contar_e_deletar_ocorrencias(meu_dicionario, minha_lista)

# print("Lista resultante:", minha_lista_resultante)
