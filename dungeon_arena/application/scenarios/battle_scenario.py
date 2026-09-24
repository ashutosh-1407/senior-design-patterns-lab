from dataclasses import dataclass
from ...domain.characters.player import Player
from ...domain.characters.dragon import Dragon


@dataclass
class BattleScenario:
    player: Player
    dragon: Dragon
    distance: float
