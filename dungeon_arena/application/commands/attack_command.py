from .command import Command
from ...domain.characters.player import Player
from ...domain.combat.attack_result import AttackResult
from ...application.validation.attack_request import AttackRequest
from ...application.validation.attack_chain import create_attack_chain
from ...domain.combat.combat_target import CombatTarget


class AttackCommand(Command):
    def __init__(self, player: Player, combo_target: CombatTarget, attack_distance: float):
        super().__init__()
        self.player = player
        self.target = combo_target
        self.attack_distance = attack_distance
        self.previous_target_health: int | None = None
        self.previous_player_mana: int | None = None
        self.has_executed: bool = False

    def execute(self) -> AttackResult:
        self.previous_target_health = self.target.health
        self.previous_player_mana = self.player.mana
        attack_request = AttackRequest(self.player, self.target, self.attack_distance)
        attack_chain = create_attack_chain()
        result = attack_chain.handle(attack_request)
        # attack_result = self.player.attack(self.dragon, self.attack_distance)
        self.has_executed = True
        return result

    def undo(self) -> None:
        if self.has_executed is True:
            self.target.health = self.previous_target_health
            self.player.mana = self.previous_player_mana
