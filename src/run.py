import time

from util import Util
from day1 import FuelCalculator
from day2 import Day2

print("Advent of Code 2019 Solutions")
print("=============================")
print()

def run(title, input, runner):
    start = time.time()
    result = runner(input)
    stop = time.time()
    elapsed = round((stop - start) * 1000, 3)

    print("{} {} ({}ms)".format(title, result, elapsed))

run("Day 1 Part 1:", map(int, Util.read_all_lines("../inputs/Day1.txt")), FuelCalculator.calculate_part1) 
run("Day 1 Part 2:", map(int, Util.read_all_lines("../inputs/Day1.txt")), FuelCalculator.calculate_part2) 
run("Day 2 Part 1:", Util.read_all_text("../inputs/Day2.txt"), Day2.calculate_part_1) 



