from .weapon import Weapon
from .ancient_axe import AncientAxe
from ..combat.damage import Damage
from ..combat.damage_type import DamageType
from ..combat.attack_result import AttackResult


class AncientAxeAdapter(Weapon):
    def __init__(self, ancient_axe: AncientAxe):
        super().__init__()
        self.ancient_axe = ancient_axe

    def attack(self, context) -> AttackResult:
        damage_amount = self.ancient_axe.strike()
        damage = Damage(damage_amount, DamageType.PHYSICAL)
        return AttackResult(True, damage, 0, None)
