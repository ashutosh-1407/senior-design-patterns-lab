import unittest

from dungeon_arena.application.battle_facade import BattleFacade
from dungeon_arena.application.equipment_factory import FireEquipmentFactory


class BattleFacadeTest(unittest.TestCase):
    def test_attack_delegates_to_the_command_flow(self) -> None:
        facade = BattleFacade(FireEquipmentFactory())

        result = facade.attack(facade.equipment_factory.create_sword(), distance=1)

        self.assertTrue(result.success)
        self.assertEqual(40, facade.dragon.health)

    def test_restart_replaces_battle_state(self) -> None:
        facade = BattleFacade(FireEquipmentFactory())
        facade.attack(facade.equipment_factory.create_sword(), distance=1)

        facade.restart()

        self.assertEqual(50, facade.dragon.health)
        self.assertEqual(10, facade.player.mana)
        self.assertEqual([], facade.command_invoker.history)


if __name__ == "__main__":
    unittest.main()
