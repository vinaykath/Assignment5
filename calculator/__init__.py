class Command:
    def execute(self, *args):
        pass

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

class CommandProcessor:
    def __init__(self):
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
        }

    def execute_command(self, command_name, *args):
        command = self.commands.get(command_name)
        if not command:
            raise ValueError(f"Command '{command_name}' not found.")
        return command.execute(*args)

def main():
    processor = CommandProcessor()
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
