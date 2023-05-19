from aside.aside import Aside


class FinanceiroHome(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Financeiro - Home',
            id='1394430',
            xpath='Financeiro - Home'
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
            painel='RD - Financeiro',
            id='218633',
            xpath='Painel Dinâmico'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class LeituraDeRetorno(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Leitura de Retorno',
            id='845808',
            xpath='Leitura de Retorno'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Remessas(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Financeiro - Painel - Remessas',
            id='1288915',
            xpath='Remessas'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Faturamento(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Faturamento - Painel',
            id='333317',
            xpath='Faturamento'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeConciliacoes(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de conciliações',
            id='1710589',
            xpath='Gerenciador de conciliações'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeFilasELotesDeEmails(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Emails - Painel',
            id='1958978',
            xpath='Gerenciador de filas e lotes de emails'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeFluxoDeCaixas(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Fluxo de Caixas',
            id='1650767',
            xpath='Gerenciador de Fluxo de Caixas'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeCentroDeCustos(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Centro de Custos',
            id='1042182',
            xpath='Gerenciador de Centro de Custos'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeCobrancas(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Cobranças',
            id='1458450',
            xpath='Gerenciador de Cobranças'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeContasAPagar(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Contas a Pagar',
            id='1878993',
            xpath='Gerenciador de Contas a Pagar'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeContasAReceber(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Contas a Receber',
            id='1171825',
            xpath='Gerenciador de Contas a Receber'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeContratos(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Contratos',
            id='1976290',
            xpath='Gerenciador de Contratos'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeInadimplencia(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de Inadimplência',
            id='1118213',
            xpath='Gerenciador de Inadimplência'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDeNfse(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de NFSE',
            id='1552812',
            xpath='Gerenciador de NFSE'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class ProgramacaoDePagamentos(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de programação de pagamentos',
            id='1391737',
            xpath='Programação de Pagamentos'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class GerenciadorDePlanoDeContas(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Gerenciador de plano de contas',
            id='462340',
            xpath='Gerenciador de Plano de contas'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class PainelDoCliente(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Financeiro - Painel - Cliente',
            id='639769',
            xpath='Painel do Cliente'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class PagSeguro(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Painel PagSeguro',
            id='1490613',
            xpath='PagSeguro'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Nf2122NfseENotaDeDebito(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Financeiro - Painel - Competencia',
            id='22857',
            xpath='NF 21/22/NFSE e Nota de débito'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class TransacoesViaCartao(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Transações via Cartão',
            id='1439721',
            xpath='Transações via Cartão'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class TransacoesViaPix(Aside):
    def __init__(self,) -> None:
        super().__init__(
            painel='Transações via PIX',
            id='1270636',
            xpath='Transações via PIX'
        )

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'
