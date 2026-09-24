from dataclasses import FrozenInstanceError
import unittest

from dungeon_arena.domain.combat.attack_context import AttackContext


class AttackContextTest(unittest.TestCase):
    def test_stores_distance_and_available_mana(self) -> None:
        context = AttackContext(distance=12.5, available_mana=8)

        self.assertEqual(12.5, context.distance)
        self.assertEqual(8, context.available_mana)

    def test_rejects_negative_distance(self) -> None:
        with self.assertRaises(ValueError):
            AttackContext(distance=-1, available_mana=8)

    def test_rejects_negative_available_mana(self) -> None:
        with self.assertRaises(ValueError):
            AttackContext(distance=12.5, available_mana=-1)

    def test_is_immutable(self) -> None:
        context = AttackContext(distance=12.5, available_mana=8)

        with self.assertRaises(FrozenInstanceError):
            context.distance = 2


if __name__ == "__main__":
    unittest.main()
