import importlib
from calculator.commands import Command  # Update this line

class Calculator:
    def __init__(self):
        self.history = []
        self.plugins = {}

    def compute(self, command: Command):
        result = command.execute()
        self.history.append(command)
        return result

    def load_plugin(self, plugin_name):
        # Dynamically load plugin from the plugins folder
        plugin_module = importlib.import_module(f"calculator.plugins.{plugin_name}")
        command_class = plugin_module.register()
        self.plugins[plugin_name] = command_class

    def create_command(self, plugin_name, *args):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name](*args)
        else:
            raise ValueError(f"No such plugin: {plugin_name}")

