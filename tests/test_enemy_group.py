import unittest

from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.combat.damage import Damage
from dungeon_arena.domain.combat.damage_type import DamageType
from dungeon_arena.domain.combat.enemy_group import EnemyGroup


class EnemyGroupTest(unittest.TestCase):
    def test_group_forwards_damage_to_all_children(self) -> None:
        first = Dragon(20, armor=0)
        second = Dragon(15, armor=0)
        group = EnemyGroup([first, second])

        group.receive_damage(Damage(5, DamageType.PHYSICAL))

        self.assertEqual(15, first.health)
        self.assertEqual(10, second.health)

    def test_group_is_alive_while_any_child_is_alive(self) -> None:
        first = Dragon(5, armor=0)
        second = Dragon(10, armor=0)
        group = EnemyGroup([first, second])

        group.receive_damage(Damage(5, DamageType.PHYSICAL))

        self.assertTrue(group.is_alive())
        group.receive_damage(Damage(5, DamageType.PHYSICAL))
        self.assertFalse(group.is_alive())

    def test_groups_do_not_share_default_children(self) -> None:
        first_group = EnemyGroup()
        second_group = EnemyGroup()
        first_group.add(Dragon(10))

        self.assertTrue(first_group.is_alive())
        self.assertFalse(second_group.is_alive())


if __name__ == "__main__":
    unittest.main()
