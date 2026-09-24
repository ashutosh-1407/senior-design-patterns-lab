from abc import ABC, abstractmethod
from ..domain.weapons.weapon import Weapon
from ..domain.weapons.elemental_weapons import FireSword, FireBow, FireStaff, IceSword, IceBow, IceStaff


class EquipmentFactory(ABC):
    @abstractmethod
    def create_sword(self) -> Weapon:
        pass

    @abstractmethod
    def create_bow(self) -> Weapon:
        pass

    @abstractmethod
    def create_staff(self) -> Weapon:
        pass

class FireEquipmentFactory(EquipmentFactory):
    def create_sword(self) -> Weapon:
        return FireSword()

    def create_bow(self) -> Weapon:
        return FireBow()

    def create_staff(self) -> Weapon:
        return FireStaff()

class IceEquipmentFactory(EquipmentFactory):
    def create_sword(self) -> Weapon:
        return IceSword()

    def create_bow(self) -> Weapon:
        return IceBow()

    def create_staff(self) -> Weapon:
        return IceStaff()
