import unittest

from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.combat.damage import Damage
from dungeon_arena.domain.combat.damage_type import DamageType


class DragonTest(unittest.TestCase):
    def test_rejects_negative_starting_health(self) -> None:
        with self.assertRaises(ValueError):
            Dragon(-1)

    def test_physical_damage_is_reduced_by_armor(self) -> None:
        dragon = Dragon(20)

        dragon.receive_damage(Damage(10, DamageType.PHYSICAL))

        self.assertEqual(13, dragon.health)

    def test_armor_prevents_physical_damage_from_becoming_healing(self) -> None:
        dragon = Dragon(10)

        dragon.receive_damage(Damage(2, DamageType.PHYSICAL))

        self.assertEqual(10, dragon.health)

    def test_magical_damage_ignores_armor(self) -> None:
        dragon = Dragon(20)

        dragon.receive_damage(Damage(5, DamageType.MAGICAL))

        self.assertEqual(15, dragon.health)

    def test_health_never_falls_below_zero(self) -> None:
        dragon = Dragon(5)

        dragon.receive_damage(Damage(100, DamageType.MAGICAL))

        self.assertEqual(0, dragon.health)
        self.assertFalse(dragon.is_alive())


if __name__ == "__main__":
    unittest.main()
