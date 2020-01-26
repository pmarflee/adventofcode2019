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
    def parse_string_as_list_of_integers(input):
        return list(map(int, input.split(',')))