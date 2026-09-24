import unittest

from dungeon_arena.domain.combat.attack_context import AttackContext
from dungeon_arena.domain.combat.damage_type import DamageType
from dungeon_arena.domain.weapons.sword import Sword
from dungeon_arena.domain.weapons.weapon import Weapon


class SwordTest(unittest.TestCase):
    def test_is_a_weapon(self) -> None:
        self.assertIsInstance(Sword(), Weapon)

    def test_attack_causes_ten_physical_damage_without_mana(self) -> None:
        result = Sword().attack(AttackContext(distance=100, available_mana=0))

        self.assertTrue(result.success)
        self.assertIsNotNone(result.damage)
        self.assertEqual(10, result.damage.amount)
        self.assertIs(DamageType.PHYSICAL, result.damage.damage_type)
        self.assertEqual(0, result.mana_cost)
        self.assertIsNone(result.failure_reason)


if __name__ == "__main__":
    unittest.main()
