from .command import Command
from ...domain.combat.attack_result import AttackResult


class CommandInvoker:
    def __init__(self):
        self.command: Command | None = None
        self.history: list[Command] = []

    def set_command(self, command: Command) -> None:
        self.command = command

    def execute(self) -> AttackResult | None:
        if self.command is None:
            return None
        command_result = self.command.execute()
        if command_result.success:
            self.history.append(self.command)
        return command_result

    def undo_last(self) -> None:
        if len(self.history) > 0:
            self.history.pop().undo()
