from abc import ABC, abstractmethod


class Aside(ABC):
    def __init__(
        self,
        painel: str,
        id: str,
    ) -> None:
        self._painel: str = painel
        self._id: str = id

    @abstractmethod
    def painel(self) -> str:
        pass

    @abstractmethod
    def id(self) -> str:
        pass

    def xpath(self) -> str:
        return f'//*[@id="{self._id}"]'
