from sly import Parser
import os
import helpers.geometry as geo
from lexer import CalcLexer

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
        p = geo.Vector(*p.func)
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

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("POINT func")
    def expr(self, p):
        p = geo.Point(*p.func)
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
