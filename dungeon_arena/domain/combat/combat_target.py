from abc import ABC, abstractmethod
from .damage import Damage


class CombatTarget(ABC):
    @abstractmethod
    def receive_damage(self, damage: Damage) -> None:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass
