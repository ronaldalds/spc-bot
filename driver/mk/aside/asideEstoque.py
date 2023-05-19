from aside.aside import Aside


class EstoqueHome(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Estoque - Home',
            id='465955',
            xpath='Estoque - Home'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class PainelDinamico(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='RD - Estoque',
            id='1947945',
            xpath='Painel Dinâmico'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Compra(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Estoque - Painel - Compra',
            id='508868',
            xpath='Compra'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Estoquista(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Painel do Estoquista',
            id='1638245',
            xpath='Estoquista'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeIds(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de IDs',
            id='1377474',
            xpath='Gerenciador de IDs'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeImobilizados(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Imobilizados',
            id='589689',
            xpath='Gerenciador de Imobilizados'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeVeiculos(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de veículos',
            id='583121',
            xpath='Gerenciador de veículos'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class PainelDeDevolucao(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Painel de Devolução',
            id='1314265',
            xpath='Painel de Devolução'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class PainelDeNotas(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Painel de Notas (NF-e / NFS-e)',
            id='1729850',
            xpath='Painel de Notas (NF-e)'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Rastreabilidade(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Painel de Rastreabilidade de Estoque',
            id='1627534',
            xpath='Rastreabilidade'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class MovimentacaoSaidas(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Estoque - Painel - Venda / Comodato',
            id='279678',
            xpath='Movimentação - Saídas'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'
