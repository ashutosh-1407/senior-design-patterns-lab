from .player_state import PlayerState


class DeadState(PlayerState):
    def attack(self) -> bool:
        return False

    def can_switch_weapon(self) -> bool:
        return False