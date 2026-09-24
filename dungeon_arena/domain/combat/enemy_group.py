from .combat_target import CombatTarget


class EnemyGroup(CombatTarget):
    def __init__(self, targets: list[CombatTarget] | None = None):
        super().__init__()
        self.targets = targets if targets is not None else []

    def add(self, target: CombatTarget) -> None:
        self.targets.append(target)

    def receive_damage(self, damage):
        for target in self.targets:
            target.receive_damage(damage)

    def is_alive(self) -> bool:
        return any(target.is_alive() for target in self.targets)
