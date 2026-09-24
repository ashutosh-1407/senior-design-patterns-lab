from dataclasses import dataclass
from .damage import Damage


@dataclass(frozen=True)
class AttackResult:
    success: bool
    damage: Damage | None
    mana_cost: int
    failure_reason: str | None

    def __post_init__(self) -> None:
        if self.mana_cost < 0:
            raise ValueError("Mana cost can't be negative")

        if self.success:
            if self.damage is None:
                raise ValueError("A successful attack must include damage")
            if self.failure_reason is not None:
                raise ValueError("A successful attack can't include a failure reason")
        else:
            if self.damage is not None:
                raise ValueError("A failed attack can't include damage")
            if self.failure_reason is None:
                raise ValueError("A failed attack must include a failure reason")
            if self.mana_cost != 0:
                raise ValueError("A failed attack can't consume mana")
