from ..domain.combat.attack_result import AttackResult


class BattleFlow:
    def run_turn(self, weapon, distance) -> AttackResult:
        self._prepare_turn()
        result = self._perform_attack(weapon, distance)
        self._process_result(result)
        self._finish_turn()
        return result
    
    def _prepare_turn(self):
        pass

    def _perform_attack(self, weapon, distance):
        pass

    def _process_result(self, result):
        pass

    def _finish_turn(self):
        pass
