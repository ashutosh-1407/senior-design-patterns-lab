from dataclasses import dataclass
from ...domain.characters.player import Player
from ...domain.combat.combat_target import CombatTarget


@dataclass(frozen=True)
class AttackRequest:
    player: Player
    target: CombatTarget
    distance: float
