from typing import Any
import trig
import cmd
from functools import reduce
import operator

# TODO: use doc comments from trig.py (see help_area_of_triangle)


class graphShell(cmd.Cmd):
    intro = "Welcome to the math shell, '?' to view a list of commands \n"
    prompt = "(math) >>> "

    def do_add(self, arg: Any):
        """Add n numbers together"""
        print(sum(parse(arg)))

    def do_subtract(self, arg: Any):
        """Subtracts n numbers from 0"""
        print(reduce(operator.sub, parse(arg)))

    def do_multiply(self, arg: Any):
        """Multiplys n numbers togther"""
        print(reduce(operator.mul, parse(arg)))

    def do_divide(self, arg: Any):
        """Divides n numbers from the first value"""
        print(reduce(operator.truediv, parse(arg)))

    def do_area_of_triangle(self, arg: Any):
        print(trig.herons(*parse(arg)))

    def do_area_of_oblique_triangle(self, arg: Any):
        print(trig.area_of_oblique_triangle(*parse(arg)))

    def do_law_of_sines(self, arg: Any):
        print(trig.law_of_sines(*parse(arg)))

    def do_law_of_cosines(self, arg: Any):
        print(trig.law_of_cosines(*parse(arg)))

    def help_area_of_triangle(self):
        print(trig.herons.__doc__)

    def do_exit(self, _: Any):
        quit()


def parse(arg):
    return tuple(map(int, arg.split()))


if __name__ == "__main__":
    graphShell().cmdloop()
