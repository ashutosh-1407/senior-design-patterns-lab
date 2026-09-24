from .attack_observer import AttackObserver
from ...domain.combat.attack_event import AttackEvent


class DamageStatistics(AttackObserver):
    def __init__(self):
        super().__init__()
        self.events = []
        self.successful_attacks = 0
        self.total_damage = 0

    def on_attack(self, event: AttackEvent) -> None:
        self.events.append(event)
        if event.success:
            self.successful_attacks += 1
            self.total_damage += event.damage_amount
