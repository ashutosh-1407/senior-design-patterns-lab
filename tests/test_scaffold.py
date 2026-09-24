import subprocess
import sys
import unittest


class ScaffoldTest(unittest.TestCase):
    def test_application_is_runnable(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "dungeon_arena"],
            check=True,
            capture_output=True,
            input="q\n",
            text=True,
        )

        self.assertIn("D U N G E O N   A R E N A", result.stdout)
        self.assertIn("A wild Dragon appears", result.stdout)
        self.assertIn("You fled the battle", result.stdout)


if __name__ == "__main__":
    unittest.main()
