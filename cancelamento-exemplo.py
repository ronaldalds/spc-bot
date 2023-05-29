from playwright.sync_api import sync_playwright
from datetime import datetime
from time import sleep
import pandas as pd
import sys
import os
from pathlib import Path
import logging

#os.chdir(Path(__file__).resolve().parent)

# instalar depois
# from bot_avisar import enviar_aviso


arquivo_log = datetime.now().strftime("logs/MK01_%d_%m_%Y.log")

logging.basicConfig(filename=arquivo_log, format='%(levelname)s - %(asctime)s - %(message)s',
                    datefmt='%d/%m/%Y - %H:%M', level=logging.INFO)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Bot_Cancelamento_MK01():

    def __init__(self, usuario):
        self.usuario = usuario

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False, chromium_sandbox=False)
        # self.browser = self.playwright.firefox.launch(headless=False, chromium_sandbox=False)
        self.context = self.browser.new_context(accept_downloads=True)

        self.page = self.context.new_page()

        self.page.goto("https://mk01.online.net.br/mk/")
        # -- REALIZA O LOGIN
        sleep(4)
        self.page.click("[placeholder=\"Nome do usuário\"]")
        # Fill [placeholder="Nome do usu�rio"]
        self.page.fill("[placeholder=\"Nome do usuário\"]", self.usuario)
        sleep(4)
        # Press Tab
        self.page.press("[placeholder=\"Nome do usuário\"]", "Tab")
        # Fill [placeholder="Senha"]
        self.page.fill("[placeholder=\"Senha\"]", "Mudar123")
        # Click button:has-text("Entrar")
        sleep(4)
        # with self.page.expect_navigation():
        # self.page.click("button:has-text(\"Entrar\")")
        # clica em entrar
        self.page.mouse.move(634, 441)
        self.page.mouse.click(634, 441)

        # -- Fecha janela do aceite
        sleep(30)
        self.page.mouse.click(946, 266)

        # -- Fecha a janela de Complete seu cadastro
        sleep(20)
        self.page.mouse.click(947, 178)

        # -- Fecha a janela de chat
        sleep(6)
        self.page.mouse.click(1062, 700)
        sleep(6)

    def __Mover_e_clicar(self, x, y):
        self.page.mouse.move(x, y)
        sleep(8)
        self.page.mouse.click(x, y)

    def __Mover_clicar_e_escrever(self, x, y, texto):
        self.page.mouse.move(x, y)
        sleep(8)
        self.page.mouse.click(x, y)
        sleep(4)
        # self.page.keyboard.insert_text(texto)
        self.page.keyboard.type(texto)
        sleep(4)

    def Cancelar_Contrato(self, tipo_da_os, relato_do_problema, Contrato,
                          CodPessoa, TipoOS, IncidenciaMulta, VencimentoMulta, ValorMulta, PlanosContas,
                          GrupoAtendimentoOS, DetalheOS, DetalhesCancelamento):
        self.tipo_da_os = str(tipo_da_os)
        self.relato_do_problema = str(relato_do_problema)
        self.Contrato = str(Contrato)
        self.CodPessoa = str(CodPessoa)
        self.TipoOS = str(TipoOS)
        self.IncidenciaMulta = str(IncidenciaMulta)
        self.ValorMulta = str(ValorMulta)
        self.PlanosContas = str(PlanosContas)
        self.GrupoAtendimentoOS = str(GrupoAtendimentoOS)
        self.DetalheOS = str(DetalheOS)
        self.VencimentoMulta = str(VencimentoMulta)
        self.DetalhesCancelamento = str(DetalhesCancelamento)

        '''
        +++++++ Cancela o contrato de forma normal +++++++
        '''

        sleep(14)  # ok

        # Clica no financeiro
        self.__Mover_e_clicar(428, 30)  # ok

        print("Clica no painel de cliente")
        self.__Mover_e_clicar(58, 600)  # ok

        # Clica no busca avan�ada
        self.__Mover_e_clicar(504, 120)  # ok

        # Clica no busca avan�ada ??
        self.__Mover_e_clicar(848, 172)  # ok

        # seleciona o Tipo de pesquisa
        self.__Mover_e_clicar(491, 417)  # ok

        # digita o c�digo da pessoa
        print(">>>> CodPessoa :: ", self.CodPessoa)
        self.__Mover_clicar_e_escrever(682, 385, self.CodPessoa)  # ok
        sleep(2)
        self.page.mouse.wheel(0, 1000)
        sleep(2)

        # Confirma a busca
        self.__Mover_e_clicar(830, 625)  # ok

        # seleciona o cliente
        self.__Mover_e_clicar(360, 240)  # ok
        self.page.mouse.dblclick(360, 240)  # ok

        # ===================================
        # -- tiver multa, cria
        if self.IncidenciaMulta == "S":
            self.CriarMulta()

        # ===================================

        # busca o contrato
        self.__Mover_e_clicar(280, 200)
        sleep(6)
        self.page.keyboard.press("Control+KeyA")
        self.page.keyboard.press("Delete")
        sleep(6)
        # self.page.keyboard.insert_text(self.Contrato)
        self.page.keyboard.type(self.Contrato)
        sleep(12)

        # seleciona o contrato
        self.__Mover_e_clicar(300, 230)

        # seleciona o CANCELAR CONTRATO
        self.__Mover_e_clicar(770, 680)

        # seleciona o MOTIVO DE CANCELAMENTO
        sleep(18)
        self.page.mouse.click(890, 292)  # 890, 292
        sleep(5)
        # self.page.keyboard.insert_text("%inadimplencia")
        self.page.keyboard.type("%inadimplencia")
        sleep(5)
        self.page.keyboard.press("Enter")
        sleep(5)
        self.page.mouse.click(372, 370)

        # escreve DETALHES DO MOTIVO DE CANCELAMENTO
        self.__Mover_clicar_e_escrever(500, 400, self.DetalhesCancelamento)

        # clica em PR�XIMO 1
        self.__Mover_e_clicar(964, 595)

        # clica em PR�XIMO 2
        self.__Mover_e_clicar(964, 595)

        # MARCA ABRIR O.S. DE RETIRADA DE EQUIPAMENTOS
        self.__Mover_e_clicar(288, 181)

        # TIPOS DE O.S.
        self.__Mover_clicar_e_escrever(474, 237, self.TipoOS)
        self.page.keyboard.press("Enter")
        self.__Mover_e_clicar(362, 317)

        # GRUPO DE ATENDIMENTO
        self.__Mover_clicar_e_escrever(710, 238, self.GrupoAtendimentoOS)
        self.page.keyboard.press("Enter")
        self.__Mover_e_clicar(576, 316)

        # DEFEITO
        self.__Mover_clicar_e_escrever(930, 238, "Nenhum problema constatado")
        self.page.keyboard.press("Enter")
        self.__Mover_e_clicar(825, 316)

        # DESCRI��O DA O.S.
        self.__Mover_clicar_e_escrever(556, 316, self.relato_do_problema)

        # clica em PR�XIMO
        self.__Mover_e_clicar(964, 595)

        # TEM CERTEZA QUE DESEJA CANCELAR ESTE CONTRATO AGORA?
        self.__Mover_e_clicar(303, 550)

        self.__Mover_e_clicar(960, 599)
        print("# CONFIRMAR? - Pronto")
        sleep(20)

    def Fecha_Navegador(self):
        # fecha o navegador
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def CriarMulta(self):
        # busca o contrato
        sleep(8)
        self.page.mouse.click(280, 200)
        sleep(5)
        self.page.keyboard.press("Control+KeyA")
        self.page.keyboard.press("Delete")
        sleep(5)
        self.page.keyboard.type(self.Contrato)
        sleep(12)

        # seleciona o contrato
        self.__Mover_e_clicar(300, 230)

        # seleciona o editar contrato
        self.__Mover_e_clicar(835, 680)

        # seleciona os contratos associados
        sleep(12)
        self.__Mover_e_clicar(272, 115)

        # inserir nova conta
        sleep(8)
        self.__Mover_e_clicar(1006, 620)

        # Descri��o da conta
        sleep(8)
        self.__Mover_clicar_e_escrever(
            560, 290, "Multa por rescisão contratual")

        # VALOR
        self.__Mover_clicar_e_escrever(447, 345, self.ValorMulta)

        # VENCIMENTO
        self.__Mover_clicar_e_escrever(542, 345, self.VencimentoMulta)

        # PARCELA
        self.__Mover_clicar_e_escrever(848, 346, "1")

        # REFER�NCIA DA UNIDADE DE PLANO DE CONTAS
        self.__Mover_clicar_e_escrever(862, 401, self.PlanosContas)
        sleep(6)
        self.page.keyboard.press("Enter")
        self.__Mover_e_clicar(525, 479)

        # PR�XIMO
        self.__Mover_e_clicar(850, 536)

        # FATURAR AGORA
        self.__Mover_e_clicar(548, 357)
        self.__Mover_e_clicar(476, 432)  # SIM

        # PROFILE
        self.__Mover_clicar_e_escrever(815, 357, "Boleto Digital - Bradesco")
        sleep(5)
        self.page.keyboard.press("Enter")
        self.__Mover_e_clicar(664, 434)

        # ADICIONAR
        # TEM CERTEZA QUE DESEJA INSERIR ESSA CONTA AGORA?
        self.__Mover_e_clicar(421, 514)

        # PR�XIMO
        self.__Mover_e_clicar(850, 536)

        # -- PROCESSO CONCLUIDO
        # CONFIRMAR
        # self.__Mover_e_clicar(815, 95)
        print("# -- CONFIRMAR MULTA")

        # -- FECHA A JANELA DE VISUALIZAR/EDITAR CONTRATO
        sleep(20)
        self.__Mover_e_clicar(1080, 61)

        print(" ====>> END- CriarMulta - 20 seg")
        sleep(20)


class Bot_Recolhimento_45d_MK01():

    def __init__(self, usuario):
        self.usuario = usuario
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(accept_downloads=True)
        self.page = self.context.new_page()
        # self.page.set_viewport_size({"width": 1366, "height": 768})

    def __move_and_click(self, x, y):
        sleep(10)
        self.page.mouse.move(x, y)
        sleep(4)
        self.page.mouse.click(x, y)
        sleep(4)

    def __type_and_click(self, text, x, y):
        sleep(10)
        self.page.keyboard.type(str(text))
        sleep(4)
        self.page.keyboard.press("Enter")
        sleep(4)
        self.page.mouse.click(x, y)
        sleep(4)

    def __click_and_write(self, text, x, y):
        sleep(10)
        self.page.mouse.click(x, y)
        sleep(4)
        self.page.keyboard.type(str(text))

    def GerarOS(self, documento, conexao, tipo_os, grupo_atendimento, relato_problema):
        self.documento = documento
        self.conexao = conexao
        self.tipo_os = tipo_os
        self.grupo_atendimento = grupo_atendimento
        self.relato_problema = relato_problema

        self.page.goto("https://mk01.online.net.br/mk/login/?sys=MK0")
        sleep(4)
        # Click [placeholder="Nome do usu�rio"]
        self.page.click("[placeholder=\"Nome do usuário\"]")
        # Fill [placeholder="Nome do usu�rio"]
        self.page.fill("[placeholder=\"Nome do usuário\"]", self.usuario)
        # Press Tab
        self.page.press("[placeholder=\"Nome do usuário\"]", "Tab")
        # Fill [placeholder="Senha"]
        self.page.fill("[placeholder=\"Senha\"]", "Mudar123")
        # Press Enter
        with self.page.expect_navigation(timeout=30000):
            self.page.press("[placeholder=\"Senha\"]", "Enter")

        # sleep(12)
        # -- Fecha a janela de Complete seu cadastro
        sleep(20)
        self.page.mouse.click(946, 176)
        # -- Fecha a janela de chat
        sleep(6)
        self.page.mouse.click(1061, 698)
        sleep(8)
        # Clica na aba para recolher
        # self.__move_and_click(1060, 700)
        # sleep(8)

        # Clica na aba para recolher
        # self.__move_and_click(1060, 700)

        # Clica em Workspace
        self.__move_and_click(482, 31)

        # Clica O.S. - Painel
        self.__move_and_click(63, 424)

        # Clica em Criar Nova O.S.
        self.__move_and_click(640, 679)

        # Clica em Nome/Documento/C�digo
        self.__move_and_click(1044, 313)
        self.__type_and_click(self.documento, 537, 391)

        # Clica em pr�ximo
        self.__move_and_click(1033, 582)

        # Clica em Conex�o Associada
        self.__move_and_click(1046, 232)
        self.__type_and_click(self.conexao, 381, 308)

        # Clica em Nivel de SLA
        self.__move_and_click(780, 297)
        self.__type_and_click("preventivo", 588, 372)

        # Clica em pr�ximo
        self.__move_and_click(1053, 582)

        # Clica em Tipo da O.S.
        self.__move_and_click(780, 187)
        self.__type_and_click(self.tipo_os, 608, 265)

        # Clica em Relato do problema
        self.__move_and_click(450, 256)
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Delete")
        self.__type_and_click(self.relato_problema, 541, 284)

        # Clica em Pr�ximo
        self.__move_and_click(1053, 582)
        # Clica em Pr�ximo
        self.__move_and_click(1054, 569)

        # Clica em Grupo de atendimento
        self.__move_and_click(613, 480)
        self.__type_and_click(self.grupo_atendimento, 316, 557)

        # Clica em Pr�ximo
        self.__move_and_click(1055, 583)

        # Finaliza a cria��o da O.S.
        self.__move_and_click(1049, 585)

        # Fecha A Janela de Aviso
        self.__move_and_click(816, 156)

        # Fecha Atendimento - OS
        self.__move_and_click(1107, 82)

    def FecharBot(self):
        sleep(4)
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def __init__(self, usuario):
        self.usuario = usuario
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(accept_downloads=True)
        self.page = self.context.new_page()

    def _mover_e_clicar(self, x, y):
        sleep(10)
        self.page.mouse.move(x, y)
        sleep(4)
        self.page.mouse.click(x, y)
        sleep(4)

    def _escrever_e_clicar(self, text, x, y):
        sleep(10)
        self.page.keyboard.type(str(text))
        sleep(4)
        self.page.keyboard.press("Enter")
        sleep(4)
        self.page.mouse.click(x, y)
        sleep(4)

    def _clicar_e_escrever(self, text, x, y):
        sleep(10)
        self.page.mouse.click(x, y)
        sleep(4)
        self.page.keyboard.type(str(text))

    def Remover_ONU(self, CodConexao):
        self.page.goto("https://mk01.online.net.br/mk/login/?sys=MK0")
        sleep(4)
        # Click [placeholder="Nome do usu�rio"]
        self.page.click("[placeholder=\"Nome do usu�rio\"]")
        # Fill [placeholder="Nome do usu�rio"]
        self.page.fill("[placeholder=\"Nome do usu�rio\"]", self.usuario)
        # Press Tab
        self.page.press("[placeholder=\"Nome do usu�rio\"]", "Tab")
        # Fill [placeholder="Senha"]
        self.page.fill("[placeholder=\"Senha\"]", "Mudar123")
        # Press Enter
        with self.page.expect_navigation(timeout=30000):
            self.page.press("[placeholder=\"Senha\"]", "Enter")

        sleep(15)
        # -- Fecha a janela de Complete seu cadastro
        sleep(10)
        self.page.mouse.click(947, 178)
        # -- Fecha a janela de chat
        sleep(8)
        self.page.mouse.click(1062, 700)
        sleep(8)
        # Clica na aba para recolher
        self.page.mouse.click(1060, 700)
        sleep(8)
        # ===================================================#
        # passos
        # aba tecnico 600, 30
        self._mover_e_clicar(600, 30)
        # busca avan�ada 879, 115
        self._mover_e_clicar(879, 115)
        # Tipo de pesquisa 806, 118
        self._mover_e_clicar(806, 118)
        # seleciona 'C�digo da conexao' 551, 303
        self._mover_e_clicar(551, 303)
        # digita o c�digo da conexao
        self._clicar_e_escrever(CodConexao, 516, 378)
        # bot�o ok 796, 658
        self._mover_e_clicar(796, 658)
        # clica na conex�o 657, 232
        self._mover_e_clicar(657, 232)
        # clica em 'Provisionar'
        self._mover_e_clicar(1224, 681)
        # seleciona o script de provisionamento 742, 253
        self._mover_e_clicar(742, 253)
        # escreve em 'remover' e filtra o script
        self.page.wait_for_timeout(4000)
        self.page.keyboard.type('remover')
        self.page.wait_for_timeout(6000)
        self.page.keyboard.press('Enter')
        self.page.wait_for_timeout(6000)
        # seleciona o script 370, 330
        self.page.mouse.click(370, 330)
        # bot�o ok 1010, 220
        # self.page.mouse.click(1010, 220)
        print('OK')

        sleep(15)
        self.context.close()
        self.browser.close()
        self.playwright.stop()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Cancelamento(usuario, arquivo_cancelamentos):
    if os.path.exists(arquivo_cancelamentos):

        Lista_cancelamentos = pd.read_csv(
            arquivo_cancelamentos, sep=';', dtype=object)
        Lista_cancelamentos.fillna(value="", inplace=True)

        Lista_user = Lista_cancelamentos.query(
            f"usuario == '{usuario}' ").reset_index(drop=True)

        print("\nRESUMO : {}".format(usuario))
        print(Lista_user['Loja'].value_counts())
        print("*" * 30)
        print(f"TOTAL: {len(Lista_user)}")
        print("\n")

        qtd = 0
        for index, info_os in Lista_user.iterrows():
            if index >= 0:

                tipo_da_os = info_os['Tipo OS']
                relato_do_problema = info_os['Relato do problema']
                Contrato = info_os['Contrato']
                CodPessoa = info_os['Cod Pessoa']
                IncidenciaMulta = info_os['Incidencia de Multa']
                ValorMulta = info_os['Valor Multa']
                VencimentoMulta = str(info_os['Data Vcto Multa Contratual'])
                PlanosContas = info_os['Planos de Contas']
                GrupoAtendimentoOS = info_os['Grupo Atendimento OS']
                DetalheOS = info_os['Detalhes Cancelamento']
                DetalhesCancelamento = info_os['Detalhes Cancelamento']

                VencimentoMulta = VencimentoMulta.replace("/", "")
                DetalhesCancelamento += "\n#Bot_MK01"
                relato_do_problema += "\n#Bot_MK01"
                DetalheOS += "\n#Bot_MK01"

                print("index: ", index)
                print("*" * 60)
                print("tipo_da_os - ", tipo_da_os)
                print("relato_do_problema - ", relato_do_problema)
                print("Contrato - ", Contrato)
                print("CodPessoa - ", CodPessoa)
                print("IncidenciaMulta - ", IncidenciaMulta)
                print("ValorMulta - ", ValorMulta)
                print("VencimentoMulta - ", VencimentoMulta)
                print("PlanosContas - ", PlanosContas)
                print("GrupoAtendimentoOS - ", GrupoAtendimentoOS)
                print("DetalheOS - ", DetalheOS)
                print("DetalhesCancelamento - ", DetalhesCancelamento)

                print("")
                BotMK01 = Bot_Cancelamento_MK01(usuario)
                try:
                    BotMK01.Cancelar_Contrato(tipo_da_os, relato_do_problema, Contrato,
                                              CodPessoa, tipo_da_os, IncidenciaMulta, VencimentoMulta, ValorMulta,
                                              PlanosContas, GrupoAtendimentoOS, DetalheOS, DetalhesCancelamento)
                    logging.info(
                        f"MK01 {usuario} | index: {index} FEITO CONTRATO: {Contrato} | CODPESSOA: {CodPessoa}  \o/")
                    qtd += 1
                except:
                    logging.error(
                        f"MK01 {usuario} | index: {index} FEITO CONTRATO: {Contrato} | CODPESSOA: {CodPessoa}  :/")
                    sleep(10)
                finally:
                    BotMK01.Fecha_Navegador()

        # endFor
        # enviar_aviso(mk=f'01 {usuario}', tipo='Cancelamento', qtd=str(qtd))


def Recolhimento(usuario, arquivo_recolhimento):
    if os.path.exists(arquivo_recolhimento):
        print("arquivo_recolhimento: ", arquivo_recolhimento)

        Lista_recolhimento = pd.read_csv(
            arquivo_recolhimento, sep=';', dtype=object)
        Lista_recolhimento.fillna(value="", inplace=True)

        Lista_user = Lista_recolhimento.query(
            f"usuario == '{usuario}' ").reset_index(drop=True)

        print("Usando o usu�rio: ", usuario)
        print("\nRESUMO")
        print(Lista_user['Grupo_Atendimento_OS'].value_counts())
        print("*" * 30)
        print(f"TOTAL: {len(Lista_user)}")
        print("\n")

        qtd = 0
        for index, info_os in Lista_user.iterrows():

            if index >= 0:
                documento = info_os['Documento/Codigo']
                conexao = info_os['Conexao Associada']
                tipo_os = info_os['Tipo OS']
                grupo_atendimento = info_os['Grupo_Atendimento_OS']
                relato_problema = info_os['Relato do problema OS']

                print("*" * 60)
                print('Index : ', index)
                print('Documento : ', documento)
                print('conexao   : ', conexao)
                print('tipo_os   : ', tipo_os)
                print('grupo_atendimento : ', grupo_atendimento)
                print('relato_problema : ', relato_problema)
                print("")

                Bot_MK01_Recolhimento = Bot_Recolhimento_45d_MK01(usuario)
                try:
                    Bot_MK01_Recolhimento.GerarOS(
                        documento, conexao, tipo_os, grupo_atendimento, relato_problema)
                    logging.info(
                        f"MK01 {usuario} Recolhimento | index: {index} | DOCUMENTO: {documento} | CONEXAO: {conexao}  \o/")
                    qtd += 1
                except:
                    logging.info(
                        f"MK01 {usuario} Recolhimento | index: {index} | DOCUMENTO: {documento} | CONEXAO: {conexao}  :/")
                    sleep(10)
                finally:
                    Bot_MK01_Recolhimento.FecharBot()

        # endfor
        # enviar_aviso(mk='01', tipo='Recolhimento', qtd=str(qtd))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# args
def main(args):

    DIA = '26'
    MES = '05'
    ANO = '2023'

    usuario = args[1]
    # usuario = 'mk.tico'
    print("Usando o usuario: ", usuario)

    Cancelamento(usuario, f"limpos/mk01_lista_cancelamento_90_dias_{DIA}_{MES}_{ANO}_limpos.csv")
    Recolhimento(usuario, f"limpos/mk01_recolhimento45d_{DIA}_{MES}_{ANO}_limpo.csv")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


if __name__ == '__main__':
    main(sys.argv)
    # main()

# source venv/bin/activate
