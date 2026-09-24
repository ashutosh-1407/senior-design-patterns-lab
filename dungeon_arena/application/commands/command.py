from abc import ABC, abstractmethod
from ...domain.combat.attack_result import AttackResult


class Command(ABC):
    @abstractmethod
    def execute(self) -> AttackResult:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass
