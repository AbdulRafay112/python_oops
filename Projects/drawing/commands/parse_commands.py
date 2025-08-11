from commands.base_command import Command 
from commands.forward_command import ForwardCommand 
from commands.turn_right_command import TurnRightCommand 
from commands.turn_left import TurnLeftCommand
def parse_commands(input_str: str) -> list[Command]:
    commands = []
    for char in input_str:
        if char == 'F':
            commands.append(ForwardCommand())
        elif char == '+':
            commands.append(TurnRightCommand())
        elif char == '-':
            commands.append(TurnLeftCommand())
    return commands 