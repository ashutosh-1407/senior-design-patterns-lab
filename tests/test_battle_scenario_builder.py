import unittest

from dungeon_arena.application.scenarios.battle_scenario import BattleScenario
from dungeon_arena.application.scenarios.battle_scenario_builder import (
    BattleScenarioBuilder,
)
from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.characters.player import Player
from dungeon_arena.domain.weapons.sword import Sword


class BattleScenarioBuilderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player(Sword(), 10)
        self.dragon = Dragon(50)

    def test_builds_scenario_with_fluent_configuration(self) -> None:
        scenario = (
            BattleScenarioBuilder()
            .with_player(self.player)
            .with_dragon(self.dragon)
            .with_distance(10)
            .build()
        )

        self.assertIsInstance(scenario, BattleScenario)
        self.assertIs(self.player, scenario.player)
        self.assertIs(self.dragon, scenario.dragon)
        self.assertEqual(10, scenario.distance)

    def test_requires_player(self) -> None:
        with self.assertRaisesRegex(ValueError, "Player is not provided"):
            BattleScenarioBuilder().with_dragon(self.dragon).with_distance(10).build()

    def test_requires_dragon(self) -> None:
        with self.assertRaisesRegex(ValueError, "Dragon is not provided"):
            BattleScenarioBuilder().with_player(self.player).with_distance(10).build()

    def test_requires_distance(self) -> None:
        with self.assertRaisesRegex(ValueError, "Distance is not provided"):
            BattleScenarioBuilder().with_player(self.player).with_dragon(self.dragon).build()


if __name__ == "__main__":
    unittest.main()
