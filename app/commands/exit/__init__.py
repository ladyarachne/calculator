from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting...")
        return True