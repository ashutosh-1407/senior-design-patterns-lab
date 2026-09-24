from .sword import Sword
from .bow import Bow
from .magic_staff import MagicStaff
from ..combat.damage import Damage
from ..combat.damage_type import DamageType
from ..combat.attack_result import AttackResult


class FireSword(Sword):
    def attack(self, context) -> AttackResult:
        result = super().attack(context)
        damage_amount = result.damage.amount
        damage = Damage(damage_amount, DamageType.FIRE)
        return AttackResult(True, damage, 0, None)

class FireBow(Bow):
    def attack(self, context) -> AttackResult:
        result = super().attack(context)
        damage_amount = result.damage.amount
        damage = Damage(damage_amount, DamageType.FIRE)
        return AttackResult(True, damage, 0, None)

class FireStaff(MagicStaff):
    def attack(self, context) -> AttackResult:
        result = super().attack(context)
        if result.success:
            damage_amount = result.damage.amount
            damage = Damage(damage_amount, DamageType.FIRE)
        else:
            damage = None
        return AttackResult(result.success, damage, result.mana_cost, result.failure_reason)

class IceSword(Sword):
    def attack(self, context) -> AttackResult:
        result = super().attack(context)
        damage_amount = result.damage.amount
        damage = Damage(damage_amount, DamageType.ICE)
        return AttackResult(True, damage, 0, None)

class IceBow(Bow):
    def attack(self, context) -> AttackResult:
        result = super().attack(context)
        damage_amount = result.damage.amount
        damage = Damage(damage_amount, DamageType.ICE)
        return AttackResult(True, damage, 0, None)

class IceStaff(MagicStaff):
    def attack(self, context) -> AttackResult:
        result = super().attack(context)
        if result.success:
            damage_amount = result.damage.amount
            damage = Damage(damage_amount, DamageType.ICE)
        else:
            damage = None
        return AttackResult(result.success, damage, result.mana_cost, result.failure_reason)
