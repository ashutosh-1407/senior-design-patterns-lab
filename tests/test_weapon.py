import unittest

from dungeon_arena.domain.weapons.weapon import Weapon


class WeaponTest(unittest.TestCase):
    def test_cannot_create_weapon_without_attack_implementation(self) -> None:
        with self.assertRaises(TypeError):
            Weapon()


if __name__ == "__main__":
    unittest.main()
