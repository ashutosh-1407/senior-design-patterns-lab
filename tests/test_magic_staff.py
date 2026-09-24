import unittest

from dungeon_arena.domain.combat.attack_context import AttackContext
from dungeon_arena.domain.combat.damage_type import DamageType
from dungeon_arena.domain.weapons.magic_staff import MagicStaff
from dungeon_arena.domain.weapons.weapon import Weapon


class MagicStaffTest(unittest.TestCase):
    def test_is_a_weapon(self) -> None:
        self.assertIsInstance(MagicStaff(), Weapon)

    def test_attack_fails_when_mana_is_insufficient(self) -> None:
        result = MagicStaff().attack(
            AttackContext(distance=100, available_mana=4)
        )

        self.assertFalse(result.success)
        self.assertIsNone(result.damage)
        self.assertEqual(0, result.mana_cost)
        self.assertEqual("Not enough mana", result.failure_reason)

    def test_attack_succeeds_with_exact_required_mana(self) -> None:
        result = MagicStaff().attack(
            AttackContext(distance=100, available_mana=5)
        )

        self.assertTrue(result.success)
        self.assertIsNotNone(result.damage)
        self.assertEqual(20, result.damage.amount)
        self.assertIs(DamageType.MAGICAL, result.damage.damage_type)
        self.assertEqual(5, result.mana_cost)
        self.assertIsNone(result.failure_reason)


if __name__ == "__main__":
    unittest.main()
