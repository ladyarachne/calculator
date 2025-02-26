class App: 
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("help", HelpCommand())

        print("Hello World. Type 'exit' to exit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())