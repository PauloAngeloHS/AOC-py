import RE

INPUT = "input/01-puzzle"
RE =

def main():
    lines = parse_input_file()
    
    result = 1


def parse_input_file():
    with open(INPUT, "r") as f:
        lines = f.read().split("\n")
    f.close()
    return lines
