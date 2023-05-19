from abc import ABC, abstractmethod


class Aside(ABC):
    def __init__(
        self,
        painel: str,
        id: str,
        xpath: str,
    ) -> None:
        self._painel: str = painel
        self._id: str = id
        self._xpath: str = xpath

    @abstractmethod
    def painel(self) -> str:
        pass

    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def xpath(self) -> str:
        pass
