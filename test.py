import pandas
import re
from datetime import datetime

def formatar_data(data):

    try:
        data_excel = int(data)
        data = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + data_excel - 2)
        data_formatada = data.strftime("%d/%m/%Y")
        return data_formatada
    except ValueError:
        try:
            formatos_data = [
            r"\d{2}/\d{2}/\d{4}",                          # formato dd/mm/yyyy
            r"\d{4}-\d{2}-\d{2}",                          # formato yyyy-mm-dd
            r"\d{4}/\d{2}/\d{2}",                          # formato yyyy/mm/dd
            r"\d{4}-\|/\d{2}-\|/\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z"  # formato yyyy-mm-ddTHH:MM:SS.000Z
            ]
            for formato in formatos_data:
                if re.match(formato, data):
                    data = datetime.strptime(data, formato)
                    data_formatada = data.strftime("%d/%m/%Y")
                    return data_formatada
        except:
            return None, "asdf"





def formatar_valor_multa(multa):
    if multa >= 0:
        return f"{float(multa):.2f}".replace(".", ",")
    else:
        return None

def formatar_incidencia(incidencia):
    # verifica se é S = a True ou N = a False
    if "S" == str(incidencia).strip():
        return True
    elif "N" == str(incidencia).strip():
        return False
    # retorna None em caso de um valor diferente de S ou N
    else:
        return None

def formatar_cpf(cpf):
    # Remover cod: deixando somente possivél cpf
    cpf = str(cpf).strip().split(" cod: ")[0]
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    # verifica se a str tem condições de ser um cpf
    try:
        if len(cpf) < 11:
            return None
    except:
        return None
    # Verificar se tem 11 dígitos numéricos
    if len(cpf) == 11:
        # Formatar como CPF (###.###.###-##)
        cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return cpf_formatado
    return None

file = pandas.read_excel('mk03.xlsx')

# for i in file.iterrows():
#     contrato = str(i[1]["Contrato"])
#     cod_pessoa = str(i[1]["Cod Pessoa"]).replace(".0", "")
#     conexao_associada = str(i[1]["Conexao Associada"]).replace(".0", "")
#     os_cancelamento_ultimos_30d = str(i[1]["OS Cancelamento Ultimos 30d"])
#     doc_cod = formatar_cpf(i[1]["Documento/Codigo"])
#     tipo_os = str(i[1]["Tipo OS"])
#     plano_de_contas = i[1]["Planos de Contas"]
#     relato_do_problema = i[1]["Relato do problema"]
#     detalhes_cancelamento = i[1]["Detalhes Cancelamento"]
#     grupo_atendimento_os = i[1]["Grupo Atendimento OS"]
#     incidencia_de_multa = formatar_incidencia(i[1]["Incidencia de Multa"])
#     valor_multa = formatar_valor_multa(i[1]["Valor Multa"])
#     data_vcto_multa_contratual = formatar_data(i[1]["Data Vcto Multa Contratual"])
#     data_a_cancelar = formatar_data(i[1]["Data a Cancelar"])
#     loja = i[1]["Loja"]
#     onu_serial = i[1]["Onu Serial"]

    # print(data_vcto_multa_contratual)
print(formatar_data("2022-12-29T16:30:00.000Z"))
print(formatar_data("2022/12/29T16:30:00.000Z"))
print(formatar_data("45086"))
print(formatar_data("2022-12-09"))
print(formatar_data("2022/12/09"))
print(formatar_data("09/12/2022"))
print(formatar_data(None))
print(formatar_data(True))
print(formatar_data(False))
print(formatar_data(""))
print(formatar_data())