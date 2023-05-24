from .aside import Aside


class EstoqueHome(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Estoque - Home', id='465955')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDinamico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='RD - Estoque', id='1947945')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class Compra(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Estoque - Painel - Compra', id='508868')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class Estoquista(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel do Estoquista',id='1638245')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeIds(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de IDs',id='1377474')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class GerenciadorDeImobilizados(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Imobilizados',id='589689')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class GerenciadorDeVeiculos(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de veículos',id='583121')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class PainelDeDevolucao(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel de Devolução',id='1314265')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class PainelDeNotas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel de Notas (NF-e / NFS-e)', id='1729850')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class Rastreabilidade(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel de Rastreabilidade de Estoque', id='1627534')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class MovimentacaoSaidas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Estoque - Painel - Venda / Comodato', id='279678')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

