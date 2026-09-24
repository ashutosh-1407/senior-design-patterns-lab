from abc import ABC, abstractmethod
from ...domain.combat.attack_event import AttackEvent


class AttackObserver(ABC):
    @abstractmethod
    def on_attack(self, event: AttackEvent) -> None:
        pass

class AttackEventPublisher:
    def __init__(self):
        super().__init__()
        self.observers = set()

    def subscribe(self, observer) -> None:
        self.observers.add(observer)

    def unsubscribe(self, observer) -> None:
        self.observers.discard(observer)

    def publish(self, event: AttackEvent) -> None:
        for obs in self.observers:
            obs.on_attack(event)
