from .weapon import Weapon
from ..combat.attack_context import AttackContext
from ..combat.attack_result import AttackResult
from ..combat.damage_type import DamageType
from ..combat.damage import Damage


class MagicStaff(Weapon):
    def attack(self, context: AttackContext) -> AttackResult:
        mana = context.available_mana
        if mana >= 5:
            damage = Damage(20, DamageType.MAGICAL)
            return AttackResult(True, damage, 5, None)
        else:
            return AttackResult(False, None, 0, "Not enough mana")
