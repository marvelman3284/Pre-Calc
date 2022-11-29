from lexer import CalcLexer
from parser import CalcParser
import sys
from os.path import exists


def idle(lexer, parser):
    while True:
        try:
            text = input("(calc) >>> ")
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))


def run_file(file, lexer, parser):
    with open(file, "r") as f:
        code = f.readlines()

    for line in code:
        parser.parse(lexer.tokenize(line))


def main(lexer, parser):
    if len(sys.argv) == 1:
        idle(lexer, parser)
    elif "scl" in sys.argv[1]:
        if not exists(sys.argv[1]):
            raise FileNotFoundError()
        run_file(sys.argv[1], lexer, parser)


if __name__ == "__main__":
    lexer = CalcLexer()
    parser = CalcParser()
    main(lexer, parser)
