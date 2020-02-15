from pathlib import Path

class Util:
    @staticmethod
    def read_all_text(path):
        return Path(path).read_text('utf-8-sig')

    @staticmethod
    def read_all_lines(path):
        with open(path, "r") as f:
            return list(f)

    @staticmethod
    def parse_csv_lines_as_list(input, value_mapper):
        return list(map(lambda x: Util.parse_csv_as_list(x, value_mapper), input.splitlines())) 

    @staticmethod
    def parse_csv_as_list(input, value_mapper):
        return list(map(value_mapper, input.split(',')))

    @staticmethod
    def parse_csv_as_list_of_integers(input):
        return Util.parse_csv_as_list(input, int)