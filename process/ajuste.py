import logging
from pathlib import Path
import os
import pandas as pd
from datetime import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")
#os.chdir(Path(__file__).resolve().parent)
#print(os.chdir(Path(__file__).resolve().parent))
#os.getcwd()
#print(os.getcwd())


def _Limpar_Dados_MK03():
    # arquivo_mk03 = datetime.now().strftime(
    #     r"download\mk03_lista_cancelamento_%d_%m_%Y.xlsx")
    arquivo_mk03 = datetime.now().strftime("download/mk03_lista_cancelamento_%d_%m_%Y.xlsx")
    print(arquivo_mk03)

    df_arquivo_mk03 = pd.read_excel(arquivo_mk03, dtype=object)

    df_arquivo_mk03['Valor Multa'] = df_arquivo_mk03['Valor Multa'].apply(
        lambda x: "{:.2f}".format(x))
    df_arquivo_mk03['Valor Multa'] = df_arquivo_mk03['Valor Multa'].astype(str)
    df_arquivo_mk03['Valor Multa'] = df_arquivo_mk03['Valor Multa'].str.replace(
        '.', ',')

    df_arquivo_mk03['Data Vcto Multa Contratual'] = df_arquivo_mk03['Data Vcto Multa Contratual'].dt.strftime(
        '%d/%m/%Y')

    df_arquivo_mk03['Detalhes Cancelamento'] = df_arquivo_mk03['Detalhes Cancelamento'].str.replace(
        "            ", "")
    df_arquivo_mk03['Relato do problema'] = df_arquivo_mk03['Relato do problema'].str.replace(
        "            ", "")

    Lojas = [
        ["LOJA CASTANHAL", 10],
        ["LOJA ABAETETUBA", 8],
        ["LOJA BAIÃO", 1],
        ["LOJA BARCARENA", 3],
        ["LOJA CORPORATIVO", 1],
        ["LOJA CASTANHAL", 1],
        ["LOJA MAGUARI", 2],
        ["LOJA MARITUBA", 16],
        ["LOJA ICOARACI", 10],
        ["LOJA MOCAJUBA", 4],
        ["LOJA MOJU", 5],
        ["LOJA TAILÂNDIA", 6],
        ["LOJA TUCURUI", 3],
        ["LOJA VIGIA", 7],
        ["LOJA TERRA ALTA", 7],
        ["LOJA VILA DOS CABANOS", 5]
    ]

    CriarOS = pd.DataFrame([])

    for cidade, qtd in Lojas:
        qtd = 50
        query = f"Loja == '{cidade}'"
        cidade_selecionada = df_arquivo_mk03.query(query)
        CriarOS = pd.concat(
            [CriarOS, cidade_selecionada[:qtd]], ignore_index=True)

    Users = []
    for i in range(len(CriarOS)):
        if (i % 2) == 0:
            Users.append('mk.tico')
        else:
            Users.append('mk.teco')

    CriarOS['usuario'] = Users

    CriarOS.to_csv(datetime.today().strftime('limpos/mk03_lista_cancelamento_90_dias_%d_%m_%Y_limpo.csv'), index=False,
                   sep=';')

    print("Limpeza em: ", arquivo_mk03)
    print("RESUMO Lojas: ")
    print(CriarOS['Loja'].value_counts())
    print("Total: ", len(CriarOS))
    print("\n")


def _Limpar_Dados_MK01():
    try:
        arquivo_mk01 = datetime.now().strftime(
            "download/mk01_lista_cancelamento_%d_%m_%Y.xlsx")
        # arquivo_mk01 = r"donwload\mk01_lista_cancelamento_%d_%m_%Y.xlsx"
        print(arquivo_mk01)

        df_arquivo_mk01 = pd.read_excel(arquivo_mk01, dtype=object)

        df_arquivo_mk01['Valor Multa'] = df_arquivo_mk01['Valor Multa'].apply(
            lambda x: "{:.2f}".format(x))
        df_arquivo_mk01['Valor Multa'] = df_arquivo_mk01['Valor Multa'].astype(
            str)
        df_arquivo_mk01['Valor Multa'] = df_arquivo_mk01['Valor Multa'].str.replace(
            '.', ',')

        # 'Atendimento Associado Mais Recente'
        # df_arquivo_mk01['Atendimento Associado Mais Recente'] = df_arquivo_mk01['Atendimento Associado Mais Recente'].str.replace('-', '.') # novo

        df_arquivo_mk01['Data Vcto Multa Contratual'] = df_arquivo_mk01['Data Vcto Multa Contratual'].dt.strftime(
            '%d/%m/%Y')

        df_arquivo_mk01['Detalhes Cancelamento'] = df_arquivo_mk01['Detalhes Cancelamento'].str.replace(
            "            ", "")
        df_arquivo_mk01['Relato do problema'] = df_arquivo_mk01['Relato do problema'].str.replace(
            "            ", "")

        # fica apenas com quem não tem atendimento
        # df_arquivo_mk01 = df_arquivo_mk01.fillna("")
        # df_arquivo_mk01 = df_arquivo_mk01.loc[df_arquivo_mk01["Atendimento Associado Mais Recente"] == ""]

        # Lojas = [
        #     ["INATIVOS", 1],
        #     ["LOJA ALCÂNTARAS", 1],
        #     ["LOJA ANAPURUS", 2],
        #     ["LOJA ARARENDÁ", 3],
        #     ["LOJA BARROQUINHA", 3],
        #     ["LOJA BOA VIAGEM", 5],
        #     ["LOJA CAIÇARA", 1],
        #     ["LOJA CAMOCIM", 12],
        #     ["LOJA CARIRÉ", 2],
        #     ["LOJA CARNAUBAL", 2],
        #     ["LOJA CRATEÚS", 2],
        #     ["LOJA GRANJA", 3],
        #     ["LOJA GRANJA INTERIOR", 2],
        #     ["LOJA GUARACIABA DO NORTE", 6],
        #     ["LOJA HIDROLÂNDIA", 3],
        #     ["LOJA IBIAPINA", 3],
        #     ["LOJA IPUEIRAS", 3],
        #     ["LOJA ITATIRA", 3],
        #     ["LOJA INDEPENDÊNCIA", 1],
        #     ["LOJA LISIEUX", 1],
        #     ["LOJA MERUOCA", 3],
        #     ["LOJA MONSENHOR TABOSA", 2],
        #     ["LOJA NOVO ORIENTE", 3],
        #     ["LOJA PEDRO II", 4],
        #     ["LOJA PIRACURUCA", 2],
        #     ["LOJA PIRIPIRI", 8],
        #     ["LOJA RERIUTABA", 2],
        #     ["LOJA SANTA QUITÉRIA", 3],
        #     ["LOJA SÃO BERNARDO", 2],
        #     ["LOJA TAMBORIL", 3],
        #     ["LOJA UBAJARA", 3],
        #     ["LOJA VARJOTA", 5],
        #     ["POTI TELECOM", 1],
        # ]

        # CriarOS = pd.DataFrame([])

        # for cidade, qtd in Lojas:
        #     query = f"Loja == '{cidade}'"
        #     cidade_selecionada = df_arquivo_mk01.query(query)
        #     qtd = qtd * 1
        #     CriarOS = pd.concat(
        #         [CriarOS, cidade_selecionada[:qtd]], ignore_index=True)

        Users = []
        for i in range(len(df_arquivo_mk01)):
            if (i % 2) == 0:
                Users.append('mk.tico')
            else:
                Users.append('mk.teco')

        df_arquivo_mk01['usuario'] = Users

        df_arquivo_mk01.dropna(subset=['Cod Pessoa'], inplace=True)

        # CriarOS.to_csv(datetime.today().strftime('./cancelados/mk01_lista_cancelamento_90_dias_30_07_2022_limpos.csv'), index=False, sep=';')
        df_arquivo_mk01.to_csv(datetime.today().strftime('limpos/mk01_lista_cancelamento_90_dias_%d_%m_%Y_limpos.csv'),
                               index=False, sep=';')

        print("RESUMO Lojas: ")
        print(df_arquivo_mk01['Loja'].value_counts())
        print("Total: ", len(df_arquivo_mk01))
        print("\n")

        print("Limpeza em: ", arquivo_mk01)
    except:
        print('ARQUIVO: Não existe')


def _Limpar_Dados_Recolhimento_MK01():
    try:
        arquivo_cancelamentos = datetime.now().strftime(
            "download/mk01_recolhimento45d_%d_%m_%Y.xlsx")

        Lista_recolhimento = pd.read_excel(arquivo_cancelamentos, dtype=object)
        # Lista_recolhimento.dropna(inplace=True)

        # REMOVE VALORES NULOS NA COLUNA 'OS Cancelamento'
        Lista_recolhimento.dropna(
            subset=['OS Cancelamento ou Recolhimento'], inplace=True)

        # REMOVE VALORES NULOS NA COLUNA 'Conexao Associada'
        Lista_recolhimento.dropna(subset=['Conexao Associada'], inplace=True)

        # RENOMEA A COLUNA
        Lista_recolhimento.rename(
            columns={'Grupo Atendimento OS': 'Grupo_Atendimento_OS'}, inplace=True)

        # apaga se Já houver O.S. de cancelamento
        indexNames = Lista_recolhimento[Lista_recolhimento['OS Cancelamento ou Recolhimento'] == 'S'].index
        Lista_recolhimento.drop(indexNames, inplace=True)

        # apaga se a quantidade de conexões for maior que 1
        indexNames = Lista_recolhimento[Lista_recolhimento['Qtd Conexoes'] > 1].index
        Lista_recolhimento.drop(indexNames, inplace=True)

        indexNames = Lista_recolhimento[Lista_recolhimento['Qtd Atendimentos'] > 0].index
        Lista_recolhimento.drop(indexNames, inplace=True)

        Users = []

        for i in range(len(Lista_recolhimento)):
            if (i % 2) == 0:
                Users.append('mk.tico')
            else:
                Users.append('mk.teco')

        Lista_recolhimento['usuario'] = Users

        print("Limpeza em: ", arquivo_cancelamentos)
        print("RESUMO: Grupo_Atendimento_OS ")
        print(Lista_recolhimento['Grupo_Atendimento_OS'].value_counts())
        print("Total: ", len(Lista_recolhimento))
        print("\n")

        Lista_recolhimento.to_csv(datetime.today().strftime(
            'limpos/mk01_recolhimento45d_%d_%m_%Y_limpo.csv'), index=False, sep=';')
    except:
        print('ARQUIVO: Não existe')


def _Limpar_Dados_Recolhimento_MK03():
    try:
        arquivo_cancelamentos = datetime.now().strftime(
            "download/mk03_recolhimento45d_%d_%m_%Y.xlsx")

        Lista_recolhimento = pd.read_excel(arquivo_cancelamentos, dtype=object)
        print(arquivo_cancelamentos)
        # REMOVE VALORES NULOS NA COLUNA 'OS Cancelamento'
        Lista_recolhimento.dropna(
            subset=['OS Cancelamento ou Recolhimento'], inplace=True)

        # RENOMEA A COLUNA
        Lista_recolhimento.rename(
            columns={'Grupo Atendimento OS': 'Grupo_Atendimento_OS'}, inplace=True)

        # apaga se Já houver O.S. de cancelamento
        indexNames = Lista_recolhimento[Lista_recolhimento['OS Cancelamento ou Recolhimento'] == 'S'].index
        Lista_recolhimento.drop(indexNames, inplace=True)

        # apaga se a quantidade de conexões for maior que 1
        indexNames = Lista_recolhimento[Lista_recolhimento['Qtd Conexoes'] > 1].index
        Lista_recolhimento.drop(indexNames, inplace=True)

        # apaga se a quantidade de atentimentos for maior que 0
        indexNames = Lista_recolhimento[Lista_recolhimento['Qtd Atendimentos'] > 0].index
        Lista_recolhimento.drop(indexNames, inplace=True)

        # Lojas = [
        #     ["LOJA CASTANHAL", 35],
        #     ["LOJA VIGIA", 15],
        #     ["LOJA TERRA ALTA", 10],
        #     ["LOJA ICOARACI", 30],
        #     ["LOJA MARITUBA", 25],
        #     ["LOJA VILA DOS CABANOS", 10],
        #     ["LOJA BARCARENA", 10],
        #     ["LOJA MAGUARI", 10],
        #     ["LOJA ABAETETUBA", 15],
        #     ["LOJA TUCURUI", 15],
        #     ["LOJA TAILÂNDIA", 10],
        #     ["LOJA MOJU", 10],
        #     ["LOJA MOCAJUBA", 10],
        #     ["LOJA BAIÃO", 10]
        # ]
        # mudança feita 03/04/2023
        Lojas = [
            ["LOJA CASTANHAL", 18],
            ["LOJA VIGIA", 5],
            ["LOJA TERRA ALTA", 5],
            ["LOJA ICOARACI", 18],
            ["LOJA MARITUBA", 20],
            ["LOJA VILA DOS CABANOS", 10],
            ["LOJA BARCARENA", 5],
            ["LOJA MAGUARI", 5],
            ["LOJA ABAETETUBA", 15],
            ["LOJA TUCURUI", 10],
            ["LOJA TAILÂNDIA", 10],
            ["LOJA MOJU", 8],
            ["LOJA MOCAJUBA", 5],
            ["LOJA BAIÃO", 5]
        ]

        CriarOS = pd.DataFrame([])

        for cidade, qtd in Lojas:
            query = f"Loja == '{cidade}'"
            cidade_selecionada = Lista_recolhimento.query(query)
            # uso 1 para manter a quantidade, caso seja necessário dobrar a quantidade é só trocar para
            qtd = qtd * 1
            CriarOS = pd.concat(
                [CriarOS, cidade_selecionada[:qtd]], ignore_index=True)

        # adiciona os usuarios mk.tico e mk.teco
        Users = []
        for i in range(len(CriarOS)):
            if (i % 2) == 0:
                Users.append('mk.tico')
            else:
                Users.append('mk.teco')

        CriarOS['usuario'] = Users

        print("Limpeza em: ", arquivo_cancelamentos)
        print("RESUMO: LOJA")
        print(CriarOS['Loja'].value_counts())
        print("Total: ", len(CriarOS))
        print("\n")

        CriarOS.to_csv(datetime.today().strftime(
            'limpos/mk03_recolhimento45d_%d_%m_%Y_limpo.csv'), index=False, sep=';')
    except:
        print('ARQUIVO: Não existe')


def Limpar_Todos_Dados():
    '''
        -> mk01_lista_cancelamento
        https://drive.google.com/drive/folders/1PU3c3CMaj8ZpviOJvx0SE8r0d7fpQ7Ds
        -> mk03_lista_cancelamento
        https://drive.google.com/drive/folders/1YZNEDChAVDzSX0LiHvNaQJMGM8zjG82Q

        -> mk01_recolhimento45d
        https://drive.google.com/drive/folders/1ZPlmQqLxIm01qOOnQ37OtTQhTIp7JkHq
        -> mk03_recolhimento45d
        https://drive.google.com/drive/folders/1axhZv6ZPQjqPqjuFU7wBpZM3UmdZzFAT
    '''
    # Cancelamento
    _Limpar_Dados_MK01()
    _Limpar_Dados_MK03()

    # recolhimento
    _Limpar_Dados_Recolhimento_MK01()
    _Limpar_Dados_Recolhimento_MK03()


Limpar_Todos_Dados()
