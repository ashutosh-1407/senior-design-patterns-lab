from .weapon import Weapon
from ..combat.attack_context import AttackContext
from ..combat.attack_result import AttackResult
from ..combat.damage import Damage


class EmpoweredWeapon(Weapon):
    def __init__(self, weapon: Weapon):
        super().__init__()
        self.weapon = weapon

    def attack(self, context: AttackContext) -> AttackResult:
        result = self.weapon.attack(context)
        if not result.success:
            return result
        else:
            damage_amount = result.damage.amount + 5
            damage = Damage(damage_amount, result.damage.damage_type)
            mana_cost = result.mana_cost
            return AttackResult(True, damage, mana_cost, None)
