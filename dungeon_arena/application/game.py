from ..domain.characters.dragon import Dragon
from ..domain.characters.player import Player
from .ui.terminal_ui import show_status, show_title, show_weapon_menu
from .weapon_factory import get_weapon
from .game_modes import GameMode, WarriorMode
from .events.attack_observer import AttackEventPublisher
from .events.battle_log import BattleLog
from ..domain.combat.attack_event import AttackEvent
from .events.damage_statistics import DamageStatistics
from .battle_facade import BattleFacade


class Game:
    def __init__(self, game_mode: GameMode | None = None):
        self.game_mode = game_mode or WarriorMode()
        self.event_publisher = AttackEventPublisher()
        self.battle_log = BattleLog()
        self.damage_statistics = DamageStatistics()

        self.event_publisher.subscribe(self.battle_log)
        self.event_publisher.subscribe(self.damage_statistics)

    def run(self) -> None:
        equipment_factory = self.game_mode.create_equipment_factory()
        battle_facade = BattleFacade(equipment_factory)
        player = battle_facade.player
        dragon = battle_facade.dragon
        # player = Player(equipment_factory.create_sword(), 10)
        # dragon = Dragon(50)

        show_title()

        while dragon.is_alive():
            show_status(dragon.health, player.mana)
            show_weapon_menu()

            choice = input("\nYour choice: ")
            if choice.lower() == "q":
                print("You fled the battle. Game Over!")
                break

            if choice == "1":
                current_weapon = equipment_factory.create_sword()
            elif choice == "2":
                current_weapon = equipment_factory.create_bow()
            elif choice == "3":
                current_weapon = equipment_factory.create_staff()
            elif choice == "4":
                current_weapon = get_weapon("ancient_axe")
            else:
                print("Invalid choice! Please select 1, 2, 3, or q.")
                continue

            # player.switch_weapon(current_weapon)

            try:
                distance = float(input("Enter distance to the Dragon: "))
            except ValueError:
                print("Please enter a valid number for distance.")
                continue

            old_dragon_health = dragon.health

            try:
                result = battle_facade.attack(current_weapon, distance)
                attack_event = AttackEvent(
                    "Player", 
                    type(player.current_weapon).__name__,
                    "Dragon",
                    result.success,
                    result.damage.amount if result.success else None,
                    result.damage.damage_type if result.success else None,
                    result.mana_cost,
                    result.failure_reason)
                self.event_publisher.publish(attack_event)
            except ValueError as error:
                print(f"Invalid attack: {error}")
                continue

            if not result.success:
                print(f"Attack Failed: {result.failure_reason}")
            else:
                current_dragon_health = dragon.health
                actual_health_lost = old_dragon_health - current_dragon_health
                print(f"💥 Success! The Dragon 🐉 lost {actual_health_lost} health.")
                print(f"🐉 Dragon Health: {dragon.health}/50")
                print(f"✨ Remaining Mana: {player.mana}/10")

            if not dragon.is_alive():
                break

        if not dragon.is_alive():
            print("\n🎉 Congratulations! You have slain the dragon!")
