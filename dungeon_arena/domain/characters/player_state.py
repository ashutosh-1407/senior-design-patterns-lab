from abc import ABC, abstractmethod


class PlayerState(ABC):
    @abstractmethod
    def attack(self) -> bool:
        pass

    @abstractmethod
    def can_switch_weapon(self) -> bool:
        pass
