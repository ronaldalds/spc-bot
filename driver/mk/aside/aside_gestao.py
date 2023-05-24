from .aside import Aside


class FinanceiroHome(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Financeiro - Home', id='1394430')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDinamico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='RD - Financeiro', id='218633')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class LeituraDeRetorno(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Leitura de Retorno', id='845808')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class Remessas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Financeiro - Painel - Remessas', id='1288915')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class Faturamento(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Faturamento - Painel', id='333317')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeConciliacoes(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de conciliações', id='1710589')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeFilasELotesDeEmails(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Emails - Painel', id='1958978')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeFluxoDeCaixas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Fluxo de Caixas', id='1650767')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeCentroDeCustos(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Centro de Custos', id='1042182')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeCobrancas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Cobranças', id='1458450')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeContasAPagar(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Contas a Pagar', id='1878993')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeContasAReceber(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Contas a Receber', id='1171825')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeContratos(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Contratos', id='1976290')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeInadimplencia(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de Inadimplência', id='1118213')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDeNfse(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de NFSE', id='1552812')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class ProgramacaoDePagamentos(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de programação de pagamentos', id='1391737')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class GerenciadorDePlanoDeContas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Gerenciador de plano de contas', id='462340')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDoCliente(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Financeiro - Painel - Cliente', id='639769')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PagSeguro(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel PagSeguro', id='1490613')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class Nf2122NfseENotaDeDebito(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Financeiro - Painel - Competencia', id='22857')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class TransacoesViaCartao(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Transações via Cartão', id='1439721')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class TransacoesViaPix(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Transações via PIX', id='1270636')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id
