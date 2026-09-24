import unittest

from dungeon_arena.application.validation.attack_chain import create_attack_chain
from dungeon_arena.application.validation.attack_request import AttackRequest
from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.characters.player import Player
from dungeon_arena.domain.weapons.sword import Sword


class AttackChainTest(unittest.TestCase):
    def test_negative_distance_stops_the_chain(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)
        request = AttackRequest(player, dragon, distance=-1)

        result = create_attack_chain().handle(request)

        self.assertFalse(result.success)
        self.assertEqual("Attack distance can't be negative", result.failure_reason)
        self.assertEqual(30, dragon.health)

    def test_valid_request_reaches_attack_handler(self) -> None:
        player = Player(Sword(), 10)
        dragon = Dragon(30)
        request = AttackRequest(player, dragon, distance=1)

        result = create_attack_chain().handle(request)

        self.assertTrue(result.success)
        self.assertEqual(23, dragon.health)


if __name__ == "__main__":
    unittest.main()
