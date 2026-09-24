from .player_state import PlayerState


class StunnedState(PlayerState):
    def attack(self) -> bool:
        return False

    def can_switch_weapon(self) -> bool:
        return True