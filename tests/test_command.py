import unittest

from dungeon_arena.application.commands.attack_command import AttackCommand
from dungeon_arena.application.commands.command_invoker import CommandInvoker
from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.characters.player import Player
from dungeon_arena.domain.weapons.sword import Sword
from dungeon_arena.domain.weapons.magic_staff import MagicStaff


class CommandTest(unittest.TestCase):
    def test_attack_command_executes_only_when_invoker_runs_it(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)
        command = AttackCommand(player, dragon, attack_distance=1)
        invoker = CommandInvoker()

        invoker.set_command(command)
        self.assertEqual(30, dragon.health)

        result = invoker.execute()

        self.assertIsNotNone(result)
        self.assertTrue(result.success)
        self.assertEqual(23, dragon.health)
        self.assertEqual([command], invoker.history)

    def test_failed_command_is_not_added_to_history(self) -> None:
        player = Player(MagicStaff(), 0)
        dragon = Dragon(30)
        command = AttackCommand(player, dragon, attack_distance=1)
        invoker = CommandInvoker()
        invoker.set_command(command)

        result = invoker.execute()

        self.assertFalse(result.success)
        self.assertEqual([], invoker.history)

    def test_attack_command_undo_restores_player_and_dragon(self) -> None:
        player = Player(MagicStaff(), 5)
        dragon = Dragon(30)
        command = AttackCommand(player, dragon, attack_distance=1)

        command.execute()
        self.assertEqual(10, dragon.health)
        self.assertEqual(0, player.mana)

        command.undo()

        self.assertEqual(30, dragon.health)
        self.assertEqual(5, player.mana)

    def test_invoker_undoes_last_successful_command(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)
        command = AttackCommand(player, dragon, attack_distance=1)
        invoker = CommandInvoker()
        invoker.set_command(command)

        invoker.execute()
        invoker.undo_last()

        self.assertEqual(30, dragon.health)
        self.assertEqual(10, player.mana)
        self.assertEqual([], invoker.history)


if __name__ == "__main__":
    unittest.main()
