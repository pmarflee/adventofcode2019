from util import Util
from intcode import Computer

class Day2:
    @staticmethod
    def calculate_part_1(input):
        program = Util.parse_string_as_list_of_integers(input)
        program[1] = 12
        program[2] = 2
        computer = Computer(program)
        computer.execute_program()
        return computer.program[0]
