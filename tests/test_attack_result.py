import unittest

from dungeon_arena.domain.combat.attack_result import AttackResult
from dungeon_arena.domain.combat.damage import Damage
from dungeon_arena.domain.combat.damage_type import DamageType


class AttackResultTest(unittest.TestCase):
    def setUp(self) -> None:
        self.damage = Damage(10, DamageType.PHYSICAL)

    def test_creates_successful_result(self) -> None:
        result = AttackResult(True, self.damage, 2, None)

        self.assertTrue(result.success)
        self.assertEqual(self.damage, result.damage)
        self.assertEqual(2, result.mana_cost)

    def test_creates_failed_result(self) -> None:
        result = AttackResult(False, None, 0, "Not enough mana")

        self.assertFalse(result.success)
        self.assertEqual("Not enough mana", result.failure_reason)

    def test_rejects_negative_mana_cost(self) -> None:
        with self.assertRaises(ValueError):
            AttackResult(True, self.damage, -1, None)

    def test_success_requires_damage(self) -> None:
        with self.assertRaises(ValueError):
            AttackResult(True, None, 0, None)

    def test_success_rejects_failure_reason(self) -> None:
        with self.assertRaises(ValueError):
            AttackResult(True, self.damage, 0, "Unexpected")

    def test_failure_rejects_damage(self) -> None:
        with self.assertRaises(ValueError):
            AttackResult(False, self.damage, 0, "Failed")

    def test_failure_requires_reason(self) -> None:
        with self.assertRaises(ValueError):
            AttackResult(False, None, 0, None)

    def test_failure_rejects_mana_cost(self) -> None:
        with self.assertRaises(ValueError):
            AttackResult(False, None, 2, "Failed")


if __name__ == "__main__":
    unittest.main()
