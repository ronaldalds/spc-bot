from driver.formatador import formatar_documento
import copy
from driver.spc.spc_driver import Spc
import os
from dotenv import load_dotenv

load_dotenv()
import os

# Obter a lista de arquivos na pasta /tmp
arquivos_temporarios = os.listdir('/tmp')

# Excluir cada arquivo temporário na lista
for arquivo_temporario in arquivos_temporarios:
    caminho_arquivo = os.path.join('/tmp', arquivo_temporario)
    os.remove(caminho_arquivo)
# instance = Spc(
#         url=os.getenv('URL_SPC'),
#         operation=os.getenv('OPERATION_SPC'),
#         password=os.getenv('PASSWORD_SPC'),
#         secret=os.getenv('SECRET_KEY_SPC'),
#         )

# instance.close()

from selenium import webdriver

# Lista para armazenar as instâncias do driver
drivers = []

# Abrir e armazenar instâncias do driver
drivers.append(webdriver.Chrome())
drivers.append(webdriver.Firefox())
# Adicione outras instâncias do driver, se necessário

# Encerrar todas as instâncias do driver
for driver in drivers:
    driver.quit()
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
