from .attack_observer import AttackObserver
from ...domain.combat.attack_event import AttackEvent


class BattleLog(AttackObserver):
    def __init__(self):
        super().__init__()
        self.events = []

    def on_attack(self, event: AttackEvent) -> None:
        self.events.append(event)
        print(f"Player {event.attacker_name} attacked dragon with a {event.weapon_name}")
