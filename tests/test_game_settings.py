import unittest

from dungeon_arena.application.game_settings import Difficulty, GameSettings


class GameSettingsTest(unittest.TestCase):
    def test_repeated_construction_returns_same_instance(self) -> None:
        first = GameSettings()
        second = GameSettings()

        self.assertIs(first, second)

    def test_settings_are_shared_and_not_reinitialized(self) -> None:
        first = GameSettings()
        first.theme = "Ice"
        first.difficulty = Difficulty.HARD

        second = GameSettings()

        self.assertEqual("Ice", second.theme)
        self.assertEqual(Difficulty.HARD, second.difficulty)


if __name__ == "__main__":
    unittest.main()
