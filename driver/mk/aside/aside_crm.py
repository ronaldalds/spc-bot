from .aside import Aside


class CrmHome(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='CRM - Home', id='454751')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDinamico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='RD - CRM', id='388243')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeInviabilidades(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Inviabilidades', id='1052995')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeFechamento(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Fechamento', id='539320')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDePosVenda(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Pós-Venda', id='213393')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeMetas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Metas', id='267807')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class GerenciadorDeComissoes(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Comissões', id='887989')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeCancelamento(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Cancelamento', id='1406061')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class MapaDeCrm(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Mapa de CRM', id='1998852')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id
