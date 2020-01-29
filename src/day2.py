from util import Util
from intcode import Computer

class Day2:
    @staticmethod
    def calculate_part_1(input):
        program = Util.parse_string_as_list_of_integers(input)
        computer = Computer(program, 12, 2)
        computer.execute_program()
        return computer.program[0]

    @staticmethod
    def calculate_part_2(input):
        program = Util.parse_string_as_list_of_integers(input)
        expected = 19690720
        for noun in range(0, 99):
            for verb in range(0, 99):
                computer = Computer(program.copy(), noun, verb)
                computer.execute_program()
                if computer.program[0] == expected:
                    return 100 * noun + verb
