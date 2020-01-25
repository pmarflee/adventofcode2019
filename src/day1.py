import math

class FuelCalculator:
    @staticmethod
    def calculate(mass):
        return math.floor(mass / 3) - 2

    @staticmethod
    def calculate_with_additional_fuel(mass):
        sum = 0
        while True:
            mass = FuelCalculator.calculate(mass)
            if mass <= 0:
                break
            sum += mass
        return sum

    @staticmethod
    def calculate_list(numbers, calculator):
        return sum(map(calculator, numbers), 0)
        
    @staticmethod
    def calculate_part1(numbers):
        return FuelCalculator.calculate_list(numbers, FuelCalculator.calculate)

    @staticmethod
    def calculate_part2(numbers):
        return FuelCalculator.calculate_list(numbers, FuelCalculator.calculate_with_additional_fuel)

