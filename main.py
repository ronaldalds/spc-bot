import time
import pandas
import multiprocessing
from coin.coin import Estoque
from aside.asideEstoque import EstoqueHome
from mk_driver import Mk
from dotenv import load_dotenv
import os
import logging
import datetime

load_dotenv()

file_log = datetime.now().strftime("logs/Cancelamento_%d_%m_%Y.log")
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format=formatter,
                    datefmt='%d/%m/%Y - %H:%M')


def cancelamento(
    contrato,
    cod_Pessoa,
    conexao_associada,
    documento_codigo,
    tipo_os,
    planos_de_contas,
    relato_do_problema,
    detalhes_cancelamento,
    grupo_atendimento_os,
    incidencia_de_multa,
    valor_multa,
    data_vcto_multa_contratual,
    data_a_cancelar,
    loja,
    onu_serial,
):

    instance = Mk(
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        url=os.getenv('URL'),
    )

    instance.login()

    time.sleep(10)
    instance.close()
    return descricao


cancelamento(
    contrato='215062',
    cod_Pessoa='177680',
    conexao_associada='228777',
    documento_codigo='033.804.802-23 cod: 177680',
    tipo_os='Cancelamento - Fibra',
    planos_de_contas='01.01.02.01 Cliente - Pessoa Física',
    relato_do_problema='''Cancelamento em razão de inadimplência superior a 75 dias, em conformidade com os artigos 90 a 100 da resolução nº 632/2014 da Anatel
            
            Observação1: Multa por quebra de contrato de R$ 75,00. Para negociar seu débito, basta entrar em contato pelo 0800-088-1111
            Observação2: MAC - FC:40:09:16:10:1C | Serial ONU - ZTEG:CF233EE2 | Caixa - TCI AF.6.3.9 | Porta - 1
            Observação3: Encerramento da OS de recolhimento de equipamentos deste contrato = Retirada Concluída''',
    detalhes_cancelamento='''Cancelamento em razão de inadimplência superior a 75 dias, em conformidade com os artigos 90 a 100 da resolução nº 632/2014 da Anatel.
            MAC: FC:40:09:16:10:1C | Serial ONU: ZTEG:CF233EE2 | Caixa: TCI AF.6.3.9 | Porta: 1 |
            Multa: R$ 75,00''',
    grupo_atendimento_os='TUCURUI',
    incidencia_de_multa='S',
    valor_multa='75',
    data_vcto_multa_contratual='13/05/2023',
    data_a_cancelar='25/03/2023',
    loja='LOJA TUCURUI',
    onu_serial='ZTEG:CF233EE2',
)


# fileProduto = pandas.read_excel('estoque.xlsx')
# lista = []

# for i in fileProduto.iterrows():
#     lista.append((
#         i[1]['PRODUTOS'],
#         i[1]['CATEGORIAS'],
#         i[1]['UND'],
#         i[1]['INATIVO'],
#         i[1]['TRABALHO'],
#         i[1]['SERIAL'],
#         i[1]['MOBILE']
#     ))

# lista = [i for i in range(20)]

# número de processos a serem criados
# num_processes = multiprocessing.cpu_count()

# cria um pool com o número de processos obtidos
# pool = multiprocessing.Pool(processes=num_processes-2)

# executa a função minha_funcao para cada cliente na lista em paralelo
# resultados = []
# for item in lista:
#     resultados.append(pool.apply_async(cadastroProduto, args=item))

# obtém os resultados de cada processo e os armazena em uma lista
# resultados = [r.get() for r in resultados]

# exibe os resultados
# print(resultados)
