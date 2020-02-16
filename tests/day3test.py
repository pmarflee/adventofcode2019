from parameterized import parameterized, parameterized_class
from src.day3 import Direction, Instruction, Day3

import unittest

class Day3ParserTests(unittest.TestCase):

    @parameterized.expand([
        ("R8", Instruction(Direction.RIGHT, 8)),
        ("U5", Instruction(Direction.UP, 5)),
        ("L5", Instruction(Direction.LEFT, 5)),
        ("D3", Instruction(Direction.DOWN, 3))
    ])
    def test_parse_instruction(self, input, expected):
        self.assertEqual(expected, Instruction.parse(input))

    @parameterized.expand([
        ("R8,U5,L5,D3\r\nU7,R6,D4,L4", [ 
            [ Instruction(Direction.RIGHT, 8),
              Instruction(Direction.UP, 5),
              Instruction(Direction.LEFT, 5),
              Instruction(Direction.DOWN, 3) ], 
            [ Instruction(Direction.UP, 7),
              Instruction(Direction.RIGHT, 6),
              Instruction(Direction.DOWN, 4),
              Instruction(Direction.LEFT, 4) ]
        ])
    ])
    def test_parse_instructions(self, input, expected):
        self.assertListEqual(expected, Instruction.parse_list(input))

@parameterized_class(
    ("input", "expected_part_1", "expected_part_2"),
    [("R8,U5,L5,D3\r\nU7,R6,D4,L4", 6, 30),
    ("R75,D30,R83,U83,L12,D49,R71,U7,L72\r\nU62,R66,U55,R34,D71,R55,D58,R83", 159, 610),
    ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\r\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135, 410)])
class Day3CalculationTests(unittest.TestCase):
    def test_calculate_part_1(self):
        self.assertEqual(self.expected_part_1, Day3.calculate_part_1(self.input))
