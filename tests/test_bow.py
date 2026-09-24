import unittest

from dungeon_arena.domain.combat.attack_context import AttackContext
from dungeon_arena.domain.combat.damage_type import DamageType
from dungeon_arena.domain.weapons.bow import Bow
from dungeon_arena.domain.weapons.weapon import Weapon


class BowTest(unittest.TestCase):
    def test_is_a_weapon(self) -> None:
        self.assertIsInstance(Bow(), Weapon)

    def test_close_attack_causes_five_physical_damage(self) -> None:
        result = Bow().attack(AttackContext(distance=9.99, available_mana=0))

        self.assertEqual(5, result.damage.amount)
        self.assertIs(DamageType.PHYSICAL, result.damage.damage_type)

    def test_attack_at_ten_or_more_causes_fifteen_damage(self) -> None:
        for distance in (10, 100):
            with self.subTest(distance=distance):
                result = Bow().attack(
                    AttackContext(distance=distance, available_mana=0)
                )

                self.assertEqual(15, result.damage.amount)
                self.assertIs(DamageType.PHYSICAL, result.damage.damage_type)
                self.assertEqual(0, result.mana_cost)


if __name__ == "__main__":
    unittest.main()
