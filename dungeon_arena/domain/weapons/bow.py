from .weapon import Weapon
from ..combat.attack_context import AttackContext
from ..combat.attack_result import AttackResult
from ..combat.damage_type import DamageType
from ..combat.damage import Damage


class Bow(Weapon):
    def attack(self, context: AttackContext) -> AttackResult:
        distance = context.distance
        damage = Damage(5 if distance < 10 else 15, DamageType.PHYSICAL)
        return AttackResult(True, damage, 0, None)
