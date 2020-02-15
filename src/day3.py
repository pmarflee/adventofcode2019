from enum import Enum
from src.util import Util

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Instruction:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

    def __eq__(self, other):
        if not isinstance(other, Instruction):
            return NotImplemented
        
        return self.direction == other.direction and self.distance == other.distance

    @staticmethod
    def parse(input):
        first_char = input[:1]
        if first_char == 'U':
            direction = Direction.UP
        elif first_char == 'D':
            direction = Direction.DOWN
        elif first_char == 'L':
            direction = Direction.LEFT
        elif first_char == 'R':
            direction = Direction.RIGHT

        return Instruction(direction, int(input[1:]))

    @staticmethod
    def parse_list(input):
        return Util.parse_csv_lines_as_list(input, Instruction.parse)