import unittest

from dungeon_arena.domain.combat.attack_context import AttackContext
from dungeon_arena.domain.combat.damage_type import DamageType
from dungeon_arena.domain.weapons.elemental_weapons import (
    FireBow,
    FireStaff,
    FireSword,
    IceBow,
    IceStaff,
    IceSword,
)


class ElementalWeaponsTest(unittest.TestCase):
    def test_fire_weapons_deal_fire_damage(self) -> None:
        context = AttackContext(distance=10, available_mana=10)

        for weapon in (FireSword(), FireBow(), FireStaff()):
            result = weapon.attack(context)
            self.assertTrue(result.success)
            self.assertEqual(DamageType.FIRE, result.damage.damage_type)

    def test_ice_weapons_deal_ice_damage(self) -> None:
        context = AttackContext(distance=10, available_mana=10)

        for weapon in (IceSword(), IceBow(), IceStaff()):
            result = weapon.attack(context)
            self.assertTrue(result.success)
            self.assertEqual(DamageType.ICE, result.damage.damage_type)

    def test_elemental_staffs_preserve_mana_failure(self) -> None:
        context = AttackContext(distance=10, available_mana=0)

        for weapon in (FireStaff(), IceStaff()):
            result = weapon.attack(context)
            self.assertFalse(result.success)
            self.assertIsNone(result.damage)
            self.assertEqual("Not enough mana", result.failure_reason)


if __name__ == "__main__":
    unittest.main()
