from .attack_handler import AttackHandler
from ...domain.combat.attack_result import AttackResult


class PerformAttackHandler(AttackHandler):
    def handle(self, request) -> AttackResult:
        return request.player.attack(request.target, request.distance)
