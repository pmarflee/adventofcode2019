class Util:
    @staticmethod
    def read_all_lines(path):
        f = open(path, "r")
        lines = list(f)
        f.close()
        return lines