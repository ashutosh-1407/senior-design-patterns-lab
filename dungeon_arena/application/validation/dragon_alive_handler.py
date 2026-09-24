from .attack_handler import AttackHandler
from ...domain.combat.attack_result import AttackResult


class DragonAliveHandler(AttackHandler):
    def handle(self, request) -> AttackResult:
        if not request.target.is_alive():
            return AttackResult(False, None, 0, "Dragon is already dead")
        return self.next_handler.handle(request)
