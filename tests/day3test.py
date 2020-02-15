from parameterized import parameterized
from src.day3 import Direction, Instruction

import unittest

class Day3Tests(unittest.TestCase):

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