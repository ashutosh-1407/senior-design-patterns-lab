from abc import ABC, abstractmethod
from ..combat.attack_context import AttackContext
from ..combat.attack_result import AttackResult


class Weapon(ABC):
    @abstractmethod
    def attack(self, context: AttackContext) -> AttackResult:
        pass
