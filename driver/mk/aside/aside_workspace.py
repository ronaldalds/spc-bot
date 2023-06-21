from .aside import Aside


class WorkspaceHome(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Workspace - Home', id='166385')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDinamico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='RD - Workspace', id='555968')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class MkbotAssistant(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='MKBot Assistant', id='1843438')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class MkbotChat(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='', id='824589')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class AgendamentoDiagnostico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Workspace - Diagnósticos - Agenda', id='759593')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class AtendimentoDiagnostico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Workspace - Diagnósticos - Atendimento', id='1414703')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id



class AtendimentoPainel(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel Atendimento', id='681671')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class OsAgenda(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Agenda das O.S.', id='58874')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class OsDiagnostico(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Workspace - Diagnósticos - OS', id='1239736')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class OsMapa(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='', id='1811217')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class OsPainel(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel O.S.', id='1117358')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PessoasOuEmpresas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Workspace - painel - pessoas', id='176177')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDeRecados(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel de Recados', id='263933')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class PainelDeTarefas(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Painel de Tarefas', id='871824')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class ChatPainel(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='Chat - Painel', id='25100')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id


class SmsPainel(Aside):
    def __init__(self,) -> None:
        super().__init__(painel='SMS - Painel', id='418523')

    def painel(self) -> str:
        return self._painel

    def id(self) -> str:
        return self._id
