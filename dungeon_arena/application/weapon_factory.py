from ..domain.weapons.weapon import Weapon
from ..domain.weapons.sword import Sword
from ..domain.weapons.bow import Bow
from ..domain.weapons.magic_staff import MagicStaff
from ..domain.weapons.ancient_axe_adapter import AncientAxeAdapter
from ..domain.weapons.ancient_axe import AncientAxe


def get_weapon(weapon_type: str) -> Weapon:
    normalized_weapon_type = weapon_type.lower().strip()
    if normalized_weapon_type == "sword":
        return Sword()
    elif normalized_weapon_type == "bow":
        return Bow()
    elif normalized_weapon_type == "magic_staff":
        return MagicStaff()
    elif normalized_weapon_type == "ancient_axe":
        return AncientAxeAdapter(AncientAxe())
    else:
        raise ValueError("Incorrect weapon type passed")
