from .damage_type import DamageType
from dataclasses import dataclass


@dataclass(frozen=True)
class Damage:
    amount: int
    damage_type: DamageType

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Amount can't be negative")
