from ...domain.characters.player import Player
from ...domain.characters.dragon import Dragon
from .battle_scenario import BattleScenario


class BattleScenarioBuilder:
    def __init__(self):
        self.player = None
        self.dragon = None
        self.distance = None

    def with_player(self, player: Player):
        self.player = player
        return self

    def with_dragon(self, dragon: Dragon):
        self.dragon = dragon
        return self

    def with_distance(self, distance: float):
        self.distance = distance
        return self

    def build(self):
        if self.player is None:
            raise ValueError("Player is not provided")
        elif self.dragon is None:
            raise ValueError("Dragon is not provided")
        elif self.distance is None:
            raise ValueError("Distance is not provided")
        return BattleScenario(self.player, self.dragon, self.distance)
