from ..domain.characters.player import Player
from ..domain.characters.dragon import Dragon
from .equipment_factory import EquipmentFactory
from .commands.command_invoker import CommandInvoker
from ..domain.weapons.weapon import Weapon
from ..domain.combat.attack_result import AttackResult
from .commands.attack_command import AttackCommand


class BattleFacade:
    def __init__(self, equipment_factory: EquipmentFactory):
        self.player = Player(equipment_factory.create_sword(), 10)
        self.dragon = Dragon(50)
        self.equipment_factory = equipment_factory
        self.command_invoker = CommandInvoker()

    def attack(self, weapon: Weapon, distance: float) -> AttackResult:
        self.player.switch_weapon(weapon)
        attack_command = AttackCommand(self.player, self.dragon, distance)
        self.command_invoker.set_command(attack_command)
        result = self.command_invoker.execute()
        return result

    def restart(self) -> None:
        self.player = Player(self.equipment_factory.create_sword(), 10)
        self.dragon = Dragon(50)
        self.command_invoker = CommandInvoker()
