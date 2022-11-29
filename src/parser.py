from sly import Parser
import os
from logic.geometry import Vector as vector
from logic.geometry import Point as point
from lexer import CalcLexer
from numpy import *
from helpers.graph import *
from helpers.symplify import *


class CalcParser(Parser):
    debugfile = "sly.out"
    tokens = CalcLexer.tokens

    precedence = (
        ("left", "+", "-"),
        ("left", "*", "/"),
        ("right", "VECTOR"),
        ("right", "UMINUS"),
        ("right", "POW"),
        ("left", "EQ"),
        ("left", "FUNC"),
    )

    def __init__(self):
        self.names = {}

    @_('NAME "=" expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_("expr")
    def statement(self, p):
        print(p.expr)

    @_("FUNC")
    def func(self, p):
        for idx, arg in enumerate(p[0]):
            if arg in self.names:
                p[0][idx] = self.names[arg]
        return p[0]

    # TODO: unpack function, replace commas w newlines?
    @_("PRINT func")
    def statement(self, p):
        for i in p.func:
            print(i)

    @_("NAME func")
    def expr(self, p):
        function = f"{p.NAME}("
        for i in p.func:
            function = function + str(i) + ","

        function = function + ")"
        return eval(function)

    @_("RUN func")
    def expr(self, p):
        lexer = CalcLexer()
        parser = CalcParser()
        file = p.func[0]
        with open(file, "r") as f:
            code = f.readlines()

        for line in code:
            parser.parse((lexer.tokenize(line)))

    # TODO: use '?' to list avalible function
    # also need to write doc comments in parser.py and in geo.py
    @_("HELP func")
    def statement(self, p):
        print(eval(f"{p.func[0]}.__doc__"))

    # TODO: custom error file to raise custom errors

    @_("TYPE func")
    def expr(self, p):
        return type(p.func[0])

    @_("expr EQ expr")
    def expr(self, p):
        return p.expr0 == p.expr1

    @_('expr "." NAME func')
    def expr(self, p):
        return (
            getattr(p.expr, p.NAME)(*p.func)
            if p.func[0] is not None
            else getattr(p.expr, p.NAME)()
        )

    @_("VECTOR func")
    def expr(self, p):
        p = vector(*p.func)
        return p

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_("expr POW expr")
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

    @_("LIST LIST")
    def expr(self, p):
        return p[0][int(p[1][0])]

    @_("LIST")
    def expr(self, p):
        return p.LIST

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("POINT func")
    def expr(self, p):
        p = point(*p.func)
        return p

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_("EXIT")
    def expr(self, p):
        quit()

    @_("CLEAR")
    def expr(self, p):
        return os.system("clear")

    @_("NAME")
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f"Undefined name '{p.NAME}'")
            return

    @_("STR")
    def expr(self, p):
        return p.STR[1:-1]
