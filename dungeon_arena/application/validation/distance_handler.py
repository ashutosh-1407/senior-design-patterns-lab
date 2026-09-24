from .attack_handler import AttackHandler
from ...domain.combat.attack_result import AttackResult


class DistanceHandler(AttackHandler):
    def handle(self, request) -> AttackResult:
        if request.distance < 0:
            return AttackResult(False, None, 0, "Attack distance can't be negative")
        return self.next_handler.handle(request)
