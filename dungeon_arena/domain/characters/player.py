from dataclasses import dataclass, field
from ..weapons.weapon import Weapon
from ..combat.attack_context import AttackContext
from ..combat.attack_result import AttackResult
from .player_state import PlayerState
from .normal_state import NormalState
from ..combat.combat_target import CombatTarget


@dataclass
class Player:
    current_weapon: Weapon
    mana: int
    current_state: PlayerState = field(default_factory=NormalState)

    def __post_init__(self) -> None:
        if self.mana < 0:
            raise ValueError("Starting mana can't be negative")

    def switch_weapon(self, weapon: Weapon) -> None:
        if self.current_state.can_switch_weapon():
            self.current_weapon = weapon

    def attack(self, target: CombatTarget, distance: float) -> AttackResult:
        if not self.current_state.attack():
            return AttackResult(False, None, 0, "Player can't attack")
        else:
            attack_context = AttackContext(distance, self.mana)
            result = self.current_weapon.attack(attack_context)
            if result.success:
                self.mana -= result.mana_cost
                target.receive_damage(result.damage)
            return result

    def change_state(self, state: PlayerState) -> None:
        self.current_state = state
