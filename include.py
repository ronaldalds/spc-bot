import pandas
import multiprocessing

from process.spc import include

include(
        "092.215.323-05",
        "07/06/2003",
        "88",
        "981273327",
        "62210000",
        "Área Rural",
        "0",
        "RUA JOSE SENA EM FRENTE A MIX PAPELARIA",
        "Área Rural de Lagoa de Santo Antônio",
        "25/05/2022",
        "27/01/2022",
        "1666633",
        "659,90"
    )
# if __name__ == '__main__':
#     fileProduto = pandas.read_excel('mk01_inclusaospc_17_05_2023.xlsx')
    lista = []

    for i in fileProduto.iterrows():
        if i[1]['Tipo de Pessoa'] == 'física':
            lista.append((
                str(i[1]['CPF/CNPJ']),  # cpf_cnpj
                str(i[1]['Data Nascimento']),  # data_nascimento
                str(i[1]['DDD']),  # ddd
                str(i[1]['Celular']),  # celular
                str(i[1]['CEP']),  # cep
                str(i[1]['Logradouro']),  # logradouro
                str(i[1]['Número']),  # número
                str(i[1]['Complemento']),  # complemento
                str(i[1]['Bairro']),  # bairro
                str(i[1]['Data Vencimento']),  # data_vencimento
                str(i[1]['Data Compra']),  # data_compra
                str(i[1]['Cod Cliente']),  # cod_cliente
                str(i[1]['Valor do Débito']).replace('.', ','),  # valor_debito
            ))



    # num_processes = multiprocessing.cpu_count() # número de processos a serem criados


    # pool = multiprocessing.Pool(processes=2) # cria um pool com o número de processos obtidos


    # resultados = [] # executa a função minha_funcao para cada cliente na lista em paralelo
    # for item in lista:
    #     resultados.append(pool.apply_async(include, args=item))


    # resultados = [r.get() for r in resultados] # obtém os resultados de cada processo e os armazena em uma lista


    # print(resultados) # exibe os resultados caso tenha return