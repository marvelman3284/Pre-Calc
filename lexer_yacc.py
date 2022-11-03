# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------

from sly import Lexer, Parser
import os


class CalcLexer(Lexer):
    tokens = {NAME, NUMBER, POW, CLEAR}
    ignore = " \t"
    literals = {"=", "+", "-", "*", "/", "(", ")"}

    # Tokens
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    POW = r"\*\*"
    CLEAR = r"(clear)"

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r"\n+")
    def newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1



class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ("left", "+", "-"),
        ("left", "*", "/"),
        ("right", "UMINUS"),
        ("left", "POW"),
        ("left", "NAMES")
        ("left", "CLEAR")
    )

    def __init__(self):
        self.names = {}

    @_('NAME "=" expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_("expr")
    def statement(self, p):
        print(p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr POW expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("CLEAR")
    def expr(self, p):
        os.system("clear")
        return 0

    @_("NAME")
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print("Undefined name '%s'" % p.NAME)
            return 0


if __name__ == "__main__":
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input("calc > ")
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
