from .combat_target import CombatTarget


class ProtectedTargetProxy(CombatTarget):
    def __init__(self, target: CombatTarget):
        super().__init__()
        self.target = target
        self.unlocked = False

    def unlock(self) -> None:
        self.unlocked = True

    def receive_damage(self, damage) -> None:
        if self.unlocked:
            return self.target.receive_damage(damage)
        else:
            raise ValueError("Object needs to be unlocked first")

    def is_alive(self) -> None:
        return self.target.is_alive()
