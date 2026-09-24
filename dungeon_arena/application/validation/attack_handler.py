from abc import ABC, abstractmethod
from ...domain.combat.attack_result import AttackResult


class AttackHandler(ABC):
    def __init__(self):
        super().__init__()
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request) -> AttackResult:
        pass
