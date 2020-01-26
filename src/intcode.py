class Computer:
    def __init__(self, program):
        self.program = program
        self.reset_program_counter()

    def reset_program_counter(self):
        self.program_counter = 0

    def get_at_position(self, offset = 0):
        return self.program[self.program_counter + offset]

    def get_value_at_position(self, offset):
        return self.program[self.get_at_position(offset)]

    def set_value(self, offset, value):
        self.program[self.get_at_position(offset)] = value

    def add(self):
        first_value = self.get_value_at_position(1)
        second_value = self.get_value_at_position(2)

        self.set_value(3, first_value + second_value)

    def multiply(self):
        first_value = self.get_value_at_position(1)
        second_value = self.get_value_at_position(2)

        self.set_value(3, first_value * second_value)

    def execute_program(self):
        self.reset_program_counter()

        while True:
            opcode = self.get_at_position()
            if opcode == 1:
                self.add()
            elif opcode == 2:
                self.multiply()
            elif opcode == 99:
                break
            self.program_counter += 4