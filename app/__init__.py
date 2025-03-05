from app.commands import CommandHandler, Command
import sys
import importlib
from dotenv import load_dotenv
import pkgutil
import os
import logging 
import logging.config


class App: 
     
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_enviroment_variables()
        self.settings.setdefault("ENVIRONMENT", "production")
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO)
        logging.info("Logging configured")

    def load_enviroment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded")
        return settings
    
    def get_environment_variable(self, env_var: str = "ENVIRONMENT"):
        return self.settings.get(env_var, None)
    
    def load_plugins(self):
        plugins_package = "app.plugins"
        plugins_path = plugins_package.replace(".", "/")
        if not os.path.exists(plugins_path):
            logging.warning(f"No plugins found in {plugins_path}")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                    self.register_plugin_commands(plugin_module, plugin_name)
                except Exception as e:
                    logging.error(f"Error loading plugin {plugin_name}: {e}")
                    
    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item != Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Registered command '{plugin_name}' from plugin '{plugin_name}'")
    
    

    def start(self):
        self.load_plugins()
        logging.info("App started")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == "exit":
                    logging.info("Exiting app")
                    sys.exit(0)
                try: 
                    self.command_handler.execute_command(cmd_input)
                except KeyError:
                    logging.error(f"Command '{cmd_input}' not found")
                    sys.exit(1)
        except KeyboardInterrupt:
            logging.info("Exiting app")
            sys.exit(0)
        finally:
            logging.info("App shutdown.")

        




if __name__ == "__main__":
    app = App().start()