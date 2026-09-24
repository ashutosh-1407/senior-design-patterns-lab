from .weapon import Weapon
from ..combat.attack_context import AttackContext
from ..combat.attack_result import AttackResult
from ..combat.damage_type import DamageType
from ..combat.damage import Damage


class Sword(Weapon):
    def attack(self, context: AttackContext) -> AttackResult:
        damage = Damage(10, DamageType.PHYSICAL)
        return AttackResult(True, damage, 0, None)
