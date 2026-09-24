from dataclasses import dataclass
from ..combat.damage import Damage
from ..combat.damage_type import DamageType
from ..combat.combat_target import CombatTarget


@dataclass
class Dragon(CombatTarget):
    health: int
    armor: int = 3

    def __post_init__(self) -> None:
        if self.health < 0:
            raise ValueError("Starting health can't be negative")
        
    def receive_damage(self, damage: Damage) -> None:
        damage_type = damage.damage_type
        damage_amount = damage.amount
        if damage_type == DamageType.PHYSICAL:
            damage_amount = max(0, damage_amount - self.armor)
        self.health = max(0, self.health - damage_amount)

    def is_alive(self) -> bool:
        return self.health > 0
