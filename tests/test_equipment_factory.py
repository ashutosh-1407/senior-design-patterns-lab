import unittest

from dungeon_arena.application.equipment_factory import (
    EquipmentFactory,
    FireEquipmentFactory,
    IceEquipmentFactory,
)
from dungeon_arena.domain.weapons.elemental_weapons import (
    FireBow,
    FireStaff,
    FireSword,
    IceBow,
    IceStaff,
    IceSword,
)


class EquipmentFactoryTest(unittest.TestCase):
    def test_fire_factory_creates_fire_family(self) -> None:
        factory: EquipmentFactory = FireEquipmentFactory()

        self.assertIsInstance(factory.create_sword(), FireSword)
        self.assertIsInstance(factory.create_bow(), FireBow)
        self.assertIsInstance(factory.create_staff(), FireStaff)

    def test_ice_factory_creates_ice_family(self) -> None:
        factory: EquipmentFactory = IceEquipmentFactory()

        self.assertIsInstance(factory.create_sword(), IceSword)
        self.assertIsInstance(factory.create_bow(), IceBow)
        self.assertIsInstance(factory.create_staff(), IceStaff)


if __name__ == "__main__":
    unittest.main()
