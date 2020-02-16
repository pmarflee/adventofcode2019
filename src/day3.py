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

class Day3:
    @staticmethod
    def get_next_position(x, y, instruction):
        if instruction.direction == Direction.UP:
            offset = 0, 1
        elif instruction.direction == Direction.DOWN:
            offset = 0, -1
        elif instruction.direction == Direction.LEFT:
            offset = -1, 0
        elif instruction.direction == Direction.RIGHT:
             offset = 1, 0
        else:
            raise Exception("Invalid direction. Direction was: {}".format(instruction.direction))

        return x + offset[0], y + offset[1]

    @staticmethod
    def add_item_to_grid(x, y, index, steps, grid):
        key = x, y
        item = grid.get(key, None)
        if item is None:
            item = { index: steps }
        elif index not in item:
            item[index] = steps
        grid[key] = item

    @staticmethod
    def create_grid(lines):
        grid = dict()
        for index, instructions in enumerate(lines, start = 1):
            x = 0
            y = 0
            steps = 0
            for instruction in instructions:
                for _ in range(instruction.distance):
                    x, y = Day3.get_next_position(x, y, instruction)
                    steps += 1
                    Day3.add_item_to_grid(x, y, index, steps, grid)
        return grid
        
    @staticmethod
    def calculate(input, calculator):
        lines = Instruction.parse_list(input)
        grid = Day3.create_grid(lines)
        best = None
        for _, (k, v) in enumerate(grid.items()):
            if len(v) == 2:
                current = calculator(k, v)
                if best is None or current < best:
                    best = current

        return best

    @staticmethod
    def calculate_part_1(input):
        return Day3.calculate(input, lambda k, _: abs(k[0]) + abs(k[1]))

    @staticmethod
    def calculate_part_2(input):
        return Day3.calculate(input, lambda _, v: sum(v.values()))