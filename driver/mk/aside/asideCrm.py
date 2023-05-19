from aside.aside import Aside


class CrmHome(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='CRM - Home', id='454751', xpath='CRM - Home')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class PainelDinamico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='RD - CRM', id='388243', xpath='Painel Dinâmico')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeInviabilidades(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Inviabilidades',
                         id='1052995', xpath='Gerenciador de Inviabilidades')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeFechamento(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Fechamento',
                         id='539320', xpath='Gerenciador de Fechamento')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDePosVenda(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Pós-Venda',
                         id='213393', xpath='Gerenciador de Pós-Venda')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeMetas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Metas',
                         id='267807', xpath='Gerenciador de Metas')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeComissoes(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Comissões',
                         id='887989', xpath='Gerenciador de Comissões')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeCancelamento(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Cancelamento',
                         id='1406061', xpath='Gerenciador de Cancelamento')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class MapaDeCrm(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Mapa de CRM',
                         id='1998852', xpath='Mapa de CRM')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'
