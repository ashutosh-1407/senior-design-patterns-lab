import unittest

from dungeon_arena.application.events.attack_observer import AttackEventPublisher
from dungeon_arena.application.events.battle_log import BattleLog
from dungeon_arena.application.events.damage_statistics import DamageStatistics
from dungeon_arena.domain.combat.attack_event import AttackEvent
from dungeon_arena.domain.combat.damage_type import DamageType


class AttackObserverTest(unittest.TestCase):
    def test_publisher_delivers_event_to_battle_log(self) -> None:
        publisher = AttackEventPublisher()
        battle_log = BattleLog()
        event = AttackEvent(
            "Player", "Sword", "Dragon", True, 7, DamageType.PHYSICAL, 0, None
        )

        publisher.subscribe(battle_log)
        publisher.publish(event)

        self.assertEqual([event], battle_log.events)

    def test_publisher_delivers_same_event_to_multiple_observers(self) -> None:
        publisher = AttackEventPublisher()
        battle_log = BattleLog()
        statistics = DamageStatistics()
        event = AttackEvent(
            "Player", "Bow", "Dragon", True, 12, DamageType.PHYSICAL, 0, None
        )

        publisher.subscribe(battle_log)
        publisher.subscribe(statistics)
        publisher.publish(event)

        self.assertEqual([event], battle_log.events)
        self.assertEqual([event], statistics.events)
        self.assertEqual(1, statistics.successful_attacks)
        self.assertEqual(12, statistics.total_damage)

        failed_event = AttackEvent(
            "Player", "Magic Staff", "Dragon", False, None, None, 0, "Not enough mana"
        )
        publisher.publish(failed_event)

        self.assertEqual(1, statistics.successful_attacks)
        self.assertEqual(12, statistics.total_damage)

    def test_unsubscribed_observer_stops_receiving_events(self) -> None:
        publisher = AttackEventPublisher()
        statistics = DamageStatistics()
        first_event = AttackEvent(
            "Player", "Sword", "Dragon", True, 7, DamageType.PHYSICAL, 0, None
        )
        second_event = AttackEvent(
            "Player", "Bow", "Dragon", True, 12, DamageType.PHYSICAL, 0, None
        )

        publisher.subscribe(statistics)
        publisher.publish(first_event)
        publisher.unsubscribe(statistics)
        publisher.publish(second_event)

        self.assertEqual(1, statistics.successful_attacks)
        self.assertEqual(7, statistics.total_damage)

if __name__ == "__main__":
    unittest.main()
