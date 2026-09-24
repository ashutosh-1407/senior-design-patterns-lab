from dataclasses import dataclass
from .damage_type import DamageType


@dataclass(frozen=True)
class AttackEvent:
    attacker_name: str
    weapon_name: str
    target_name: str
    success: bool
    damage_amount: float | None
    damage_type: DamageType | None
    mana_spent: int
    failure_reason: str | None

    def __post_init__(self) -> None:
        if self.mana_spent < 0:
            raise ValueError("Mana spent can't be negative")
        if self.damage_amount is not None and self.damage_amount < 0:
            raise ValueError("Damage amount can't be negative")

        if self.success:
            if self.damage_amount is None or self.damage_type is None:
                raise ValueError("A successful event must include damage details")
            if self.failure_reason is not None:
                raise ValueError("A successful event can't include a failure reason")
        else:
            if self.damage_amount is not None or self.damage_type is not None:
                raise ValueError("A failed event can't include damage details")
            if self.failure_reason is None:
                raise ValueError("A failed event must include a failure reason")
            if self.mana_spent != 0:
                raise ValueError("A failed event can't spend mana")
