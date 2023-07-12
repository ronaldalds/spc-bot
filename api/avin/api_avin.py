import requests
import os
from dotenv import load_dotenv

load_dotenv()

class APIavin:
    def __init__(self):
        self._headers = {
            'apikey': os.getenv('APIKEY'),
            'secretkey': os.getenv('SECRETKEY')
        }

    def alerts_period(self, inicial, final):
        response = requests.get(f"https://ws.fulltrack2.com/alerts/period/initial/{inicial}/final/{final}", headers=self._headers)
        if response.status_code == 200:
            data = response.json()
            try:
                for ocorrencia in data['data']:
                    if ocorrencia['ras_eal_id_alerta_tipo'] == '46':
                        alerts = self.__veiculo_id(ocorrencia['ras_eal_id_veiculo'], inicial, final)
                return alerts
            except:
                return False
        else:
            raise Exception(f'Error ao obeter alerts API {response.status_code}')

    def __veiculo_id(self, id, inicial, final):
        response = requests.get(f"https://ws.fulltrack2.com/events/interval/id/{id}/begin/{inicial}/end/{final}", headers=self._headers)
        if response.status_code == 200:
            data = response.json()
            alerts_velocidade = []
            for alert in data['data']:
                # print(alert)
                velocidade = alert['ras_eve_velocidade']
                if int(velocidade) >= 100:
                    ocorrencia = {}
                    ocorrencia['veiculo'] = f"{alert['ras_vei_veiculo']} - {alert['ras_vei_placa']}"
                    ocorrencia['data'] = alert['ras_eve_data_gps']
                    ocorrencia['velocidade'] = alert['ras_eve_velocidade']
                    alerts_velocidade.append(ocorrencia)
            return alerts_velocidade
        
        else:
            raise Exception(f'Error ao obeter veiculo API {response.status_code}')