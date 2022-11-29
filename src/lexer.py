from sly import Lexer
import re


class CalcLexer(Lexer):
    tokens = {
        FUNC,
        LIST,
        HELP,
        NUMBER,
        STR,
        EQ,
        POW,
        EXIT,
        CLEAR,
        POINT,
        VECTOR,
        TYPE,
        PRINT,
        NAME,
        RUN,
    }
    ignore = " \t"
    ignore_comment = r"\#.*"
    literals = {".", "=", "+", "-", "*", "/", "?", "(", ")", ","}

    # Tokens
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    POW = r"\*\*"
    EQ = r"=="
    STR = r'".*"'
    NAME["vector"] = VECTOR
    NAME["clear"] = CLEAR
    NAME["exit"] = EXIT
    NAME["point"] = POINT
    NAME["type"] = TYPE
    NAME["help"] = HELP
    NAME["print"] = PRINT
    NAME["run"] = RUN

    @_(r"(\d+\.\d+)|(\d+)")
    def NUMBER(self, t):
        t.value = float(t.value) if "." in t.value else int(t.value)
        return t

    @_(r"\(([a-zA-Z0-9_\, ])*(\".*\")*\)")
    def FUNC(self, t):
        t.value = re.sub(r"[() ]", "", t.value)
        values = []

        if len(t.value) == 0:
            values.append(None)
            t.value = values
            return t

        for i in t.value.split(","):
            try:
                values.append(int(i))
            except Exception:
                if i[0] == '"' and i[-1] == '"':
                    i = re.sub(r"[\"]", "", i)
                values.append(str(i))
        t.value = values
        return t

    @_(r"(\[([a-zA-Z0-9\, ])*(\".*\")*\])")
    def LIST(self, t):
        t.value = re.sub(r"[\[\] ]", "", t.value)
        values = []

        if len(t.value) == 0:
            t.value = []
            return t

        for i in t.value.split(","):
            if i[0] == '"' and i[-1] == '"':
                i = re.sub(r"[\"]", "", i)
                values.append(str(i))
            elif re.match(r"\d", i):
                values.append(int(i))
            else:
                values.append(i)

        t.value = values
        return t

    @_(r"(\n|;)+")
    def newline(self, t):
        self.lineno += t.value.count(";") if ";" in t.value else t.value.count("\n")

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
