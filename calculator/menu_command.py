from __init__ import Command
from __init__ import AddCommand, SubtractCommand,MultiplyCommand, DivideCommand



class MenuCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self, *args):
        return "Available commands: " + ", ".join(self.commands.keys())

class CommandProcessor:
    def __init__(self):
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
            'menu': MenuCommand(self.commands),
        }

    def execute_command(self, command_name, *args):
        command = self.commands.get(command_name)
        if not command:
            raise ValueError(f"Command '{command_name}' not found.")
        return command.execute(*args)

def main():
    processor = CommandProcessor()
    print(processor.execute_command('menu'))
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        parts = user_input.split()
        command_name = parts[0]
        args = list(map(float, parts[1:]))
        try:
            result = processor.execute_command(command_name, *args)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()