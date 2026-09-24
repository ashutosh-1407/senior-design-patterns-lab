import unittest

from dungeon_arena.domain.characters.dragon import Dragon
from dungeon_arena.domain.combat.damage import Damage
from dungeon_arena.domain.combat.damage_type import DamageType
from dungeon_arena.domain.combat.protected_target_proxy import ProtectedTargetProxy


class ProtectedTargetProxyTest(unittest.TestCase):
    def test_locked_proxy_blocks_damage(self) -> None:
        dragon = Dragon(20, armor=0)
        proxy = ProtectedTargetProxy(dragon)

        with self.assertRaisesRegex(ValueError, "needs to be unlocked"):
            proxy.receive_damage(Damage(5, DamageType.PHYSICAL))

        self.assertEqual(20, dragon.health)

    def test_unlocked_proxy_forwards_damage(self) -> None:
        dragon = Dragon(20, armor=0)
        proxy = ProtectedTargetProxy(dragon)
        proxy.unlock()

        proxy.receive_damage(Damage(5, DamageType.PHYSICAL))

        self.assertEqual(15, dragon.health)
        self.assertTrue(proxy.is_alive())


if __name__ == "__main__":
    unittest.main()
