from .player_state import PlayerState


class NormalState(PlayerState):
    def attack(self) -> bool:
        return True

    def can_switch_weapon(self) -> bool:
        return True
