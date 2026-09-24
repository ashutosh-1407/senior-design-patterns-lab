import unittest

from dungeon_arena.application.battle_flow import BattleFlow
from dungeon_arena.domain.combat.attack_result import AttackResult


class SpyBattleFlow(BattleFlow):
    def __init__(self) -> None:
        self.calls: list[str] = []

    def _prepare_turn(self) -> None:
        self.calls.append("prepare")

    def _perform_attack(self, weapon, distance) -> AttackResult:
        self.calls.append("attack")
        return AttackResult(False, None, 0, "test result")

    def _process_result(self, result: AttackResult) -> None:
        self.calls.append("process")

    def _finish_turn(self) -> None:
        self.calls.append("finish")


class BattleFlowTest(unittest.TestCase):
    def test_template_method_preserves_hook_order(self) -> None:
        flow = SpyBattleFlow()

        result = flow.run_turn("Sword", 10)

        self.assertFalse(result.success)
        self.assertEqual(["prepare", "attack", "process", "finish"], flow.calls)


if __name__ == "__main__":
    unittest.main()
