from abc import ABC, abstractmethod


class Coin(ABC):
    def __init__(
        self,
        title: str,
        id: str,
        xpath: str,
    ) -> None:
        self._title: str = title
        self._id: str = id
        self._xpath: str = xpath

    @abstractmethod
    def title(self) -> str:
        pass

    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def xpath(self) -> str:
        pass


class Crm(Coin):
    def __init__(self) -> None:
        super().__init__(title="CRM", id="1791381", xpath='CRM')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Gestao(Coin):
    def __init__(self) -> None:
        super().__init__(title="Gestão", id="1856707", xpath='Gestão')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Financeiro(Coin):
    def __init__(self) -> None:
        super().__init__(title="Financeiro", id="946094", xpath='Financeiro')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Workspace(Coin):
    def __init__(self) -> None:
        super().__init__(title="Workspace", id="1833270", xpath='Workspace')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Estoque(Coin):
    def __init__(self) -> None:
        super().__init__(title="Estoque", id="1200344", xpath='Estoque')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Tecnico(Coin):
    def __init__(self) -> None:
        super().__init__(title="Técnico", id="1511788", xpath='Técnico')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Integradores(Coin):
    def __init__(self) -> None:
        super().__init__(title="Integradores", id="169073", xpath='Integradores')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Maps(Coin):
    def __init__(self) -> None:
        super().__init__(title="Maps", id="1162115", xpath='Maps')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Suporte(Coin):
    def __init__(self) -> None:
        super().__init__(title="Suporte", id="1631783", xpath='Suporte')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Ajuda(Coin):
    def __init__(self) -> None:
        super().__init__(title="Ajuda", id="1185636", xpath='Ajuda')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Home(Coin):
    def __init__(self) -> None:
        super().__init__(title="Home", id="1504596", xpath='Home')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'


class Configuracoes(Coin):
    def __init__(self) -> None:
        super().__init__(title="Configurações", id="545976", xpath='Configurações')
    
    def title(self) -> str:
        return self._title

    def id(self) -> str:
        return self._id

    def xpath(self) -> str:
        return f'//a[@title="{self._xpath}"]'