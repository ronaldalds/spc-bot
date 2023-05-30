import re
from datetime import datetime, timedelta

def formatar_data(data):
    if len(data) == 5:
        data = datetime(1899, 12, 30) + timedelta(days=int(data))
        return data.strftime("%d/%m/%Y")
    else:
        df = re.compile("([0-9]{2,4})[-]?[/]?([0-9]{2})[-]?[/]?([0-9]{2,4})")
        data = df.findall(data)[0]
        if len(data[2]) == 2:
            return f"{data[2]}/{data[1]}/{data[0]}"
        
        return f"{data[0]}/{data[1]}/{data[2]}"

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