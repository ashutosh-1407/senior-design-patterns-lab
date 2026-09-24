from abc import ABC, abstractmethod
from ..domain.weapons.weapon import Weapon
from ..domain.weapons.sword import Sword
from ..domain.weapons.bow import Bow
from ..domain.weapons.magic_staff import MagicStaff
from .equipment_factory import EquipmentFactory, FireEquipmentFactory, IceEquipmentFactory


class GameMode(ABC):
    @abstractmethod
    def create_starting_weapon(self) -> Weapon:
        pass

    @abstractmethod
    def create_equipment_factory(self) -> EquipmentFactory:
        pass

class WarriorMode(GameMode):
    def create_starting_weapon(self) -> Weapon:
        return Sword()

    def create_equipment_factory(self) -> EquipmentFactory:
        return FireEquipmentFactory()

class ArcherMode(GameMode):
    def create_starting_weapon(self) -> Weapon:
        return Bow()

    def create_equipment_factory(self) -> EquipmentFactory:
        return IceEquipmentFactory()
    
class MageMode(GameMode):
    def create_starting_weapon(self) -> Weapon:
        return MagicStaff()

    def create_equipment_factory(self) -> EquipmentFactory:
        return FireEquipmentFactory()
