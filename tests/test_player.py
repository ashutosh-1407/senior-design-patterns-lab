import unittest

from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.characters.player import Player
from dungeon_arena.domain.weapons.bow import Bow
from dungeon_arena.domain.weapons.magic_staff import MagicStaff
from dungeon_arena.domain.weapons.sword import Sword
from dungeon_arena.domain.characters.stunned_state import StunnedState
from dungeon_arena.domain.characters.dead_state import DeadState
from dungeon_arena.domain.combat.enemy_group import EnemyGroup


class PlayerTest(unittest.TestCase):
    def test_rejects_negative_starting_mana(self) -> None:
        with self.assertRaises(ValueError):
            Player(Sword(), -1)

    def test_sword_attack_damages_dragon_without_spending_mana(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)

        result = player.attack(dragon, distance=1)

        self.assertTrue(result.success)
        self.assertEqual(23, dragon.health)
        self.assertEqual(10, player.mana)

    def test_successful_magic_attack_spends_mana(self) -> None:
        player = Player(MagicStaff(), 5)
        dragon = Dragon(30)

        result = player.attack(dragon, distance=1)

        self.assertTrue(result.success)
        self.assertEqual(10, dragon.health)
        self.assertEqual(0, player.mana)

    def test_failed_attack_changes_neither_dragon_nor_mana(self) -> None:
        player = Player(MagicStaff(), 4)
        dragon = Dragon(30)

        result = player.attack(dragon, distance=1)

        self.assertFalse(result.success)
        self.assertEqual(30, dragon.health)
        self.assertEqual(4, player.mana)

    def test_switching_weapon_changes_attack_strategy(self) -> None:
        player = Player(Sword(), 0)
        dragon = Dragon(30)

        player.switch_weapon(Bow())
        player.attack(dragon, distance=10)

        self.assertEqual(18, dragon.health)

    def test_stunned_player_cannot_attack(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)
        player.change_state(StunnedState())

        result = player.attack(dragon, distance=1)

        self.assertFalse(result.success)
        self.assertEqual("Player can't attack", result.failure_reason)
        self.assertEqual(30, dragon.health)
        self.assertEqual(10, player.mana)

    def test_dead_player_cannot_attack(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)
        player.change_state(DeadState())

        result = player.attack(dragon, distance=1)

        self.assertFalse(result.success)
        self.assertEqual("Player can't attack", result.failure_reason)
        self.assertEqual(30, dragon.health)
        self.assertEqual(10, player.mana)

    def test_attack_behavior_changes_when_player_state_changes(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(50)

        normal_result = player.attack(dragon, distance=1)
        player.change_state(StunnedState())
        stunned_result = player.attack(dragon, distance=1)
        player.change_state(DeadState())
        dead_result = player.attack(dragon, distance=1)

        self.assertTrue(normal_result.success)
        self.assertFalse(stunned_result.success)
        self.assertFalse(dead_result.success)
        self.assertEqual(43, dragon.health)

    def test_stunned_player_can_switch_weapon(self) -> None:
        player = Player(Sword(), 10)
        player.change_state(StunnedState())

        player.switch_weapon(Bow())

        self.assertIsInstance(player.current_weapon, Bow)

    def test_dead_player_cannot_switch_weapon(self) -> None:
        player = Player(Sword(), 10)
        player.change_state(DeadState())

        player.switch_weapon(Bow())

        self.assertIsInstance(player.current_weapon, Sword)

    def test_player_can_attack_an_enemy_group(self) -> None:
        player = Player(Sword(), 10)
        first_dragon = Dragon(30, armor=0)
        second_dragon = Dragon(25, armor=0)
        group = EnemyGroup([first_dragon, second_dragon])

        result = player.attack(group, distance=1)

        self.assertTrue(result.success)
        self.assertEqual(20, first_dragon.health)
        self.assertEqual(15, second_dragon.health)


if __name__ == "__main__":
    unittest.main()
