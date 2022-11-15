from lexer import CalcLexer
from parser import CalcParser


def main():
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input("(calc) >>> ")
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))


if __name__ == "__main__":
    main()
