from dataclasses import dataclass


@dataclass(frozen=True)
class AttackContext:
    distance: float
    available_mana: int

    def __post_init__(self) -> None:
        if self.distance < 0:
            raise ValueError("Distance can't be negative")
        if self.available_mana < 0:
            raise ValueError("Available mana can't be negative")
