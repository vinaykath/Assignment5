import importlib
import os

class CommandProcessor:
    def __init__(self):
        self.commands = {}
        self.load_plugins()

    def load_plugins(self):
        plugin_folder = 'plugins'
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = importlib.import_module(f"{plugin_folder}.{module_name}")
                self.commands.update(module.get_commands())

    def execute_command(self, command_name, *args):
        command = self.commands.get(command_name)
        if not command:
            raise ValueError(f"Command '{command_name}' not found.")
        return command.execute(*args)
    
class Command:
    def execute(self, *args):
        pass

# Example plugin (plugins/addition.py)
class AddCommand(Command):
    def execute(self, *args):
        return sum(args)

class SubtractCommand(Command):
    def execute(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

class MultiplyCommand(Command):
    def execute(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

class DivideCommand(Command):
    def execute(self, *args):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    
def get_commands():
    return {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
        }
    
