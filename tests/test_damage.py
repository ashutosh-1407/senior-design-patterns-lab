from dataclasses import FrozenInstanceError
import unittest

from dungeon_arena.domain.combat.damage import Damage
from dungeon_arena.domain.combat.damage_type import DamageType


class DamageTest(unittest.TestCase):
    def test_stores_amount_and_type(self) -> None:
        damage = Damage(10, DamageType.PHYSICAL)

        self.assertEqual(10, damage.amount)
        self.assertIs(DamageType.PHYSICAL, damage.damage_type)

    def test_rejects_negative_amount(self) -> None:
        with self.assertRaises(ValueError):
            Damage(-1, DamageType.MAGICAL)

    def test_is_immutable(self) -> None:
        damage = Damage(10, DamageType.PHYSICAL)

        with self.assertRaises(FrozenInstanceError):
            damage.amount = 20


if __name__ == "__main__":
    unittest.main()
