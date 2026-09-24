from .battle_flow import BattleFlow
from .battle_facade import BattleFacade


class StandardBattleFlow(BattleFlow):
    def __init__(self, battle_facade: BattleFacade):
        super().__init__()
        self.battle_facade = battle_facade

    def _perform_attack(self, weapon, distance):
        return self.battle_facade.attack(weapon, distance)
