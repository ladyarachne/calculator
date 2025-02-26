from app.commands import Command


class HelpCommand(Command):
    def execute(self):
        print("Available commands:")
        for command in self.app.commands:
            print(f"- {command}")
        return False