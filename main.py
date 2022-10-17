import os
from typing import Any
from functools import reduce
from rich import print

import cmd
import operator

import trig
import graph

# TODO: use doc comments from trig.py (see help_area_of_triangle)


class graphShell(cmd.Cmd):
    intro = "Welcome to the math shell, '?' to view a list of commands \n"
    prompt = "(math) >>> "

    def do_add(self, arg: Any):
        """Add n numbers together"""
        print(sum(parse(arg)))

    def do_subtract(self, arg: Any):
        """Subtracts n numbers from each other"""
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

    def do_graph(self, arg: Any):
        if not arg:
            arg = input("Enter the equation: ")

        start = int(input("Enter the start for the range: "))
        stop = int(input("Enter the stop for the  range: "))
        num_points = [start, stop]

        graph.graph_eq(arg, num_points)

    def help_graph(self):
        print(graph.graph_eq.__doc__)

    def help_area_of_triangle(self):
        print(trig.herons.__doc__)

    def do_clear(self, _: Any):
        """
        Clears the screen
        """
        os.system("cls" if os.name == "nt" else "clear")

    def do_exit(self, _: Any):
        quit()

    # NOTE: for the solve eq function check if there are args and if not ask for the eq
    # NOTE: also make sure to print to the user to use the variable x (include in doc string?)


def parse(arg):
    return tuple(map(int, arg.split()))


if __name__ == "__main__":
    while True:
        try:
            graphShell().cmdloop()
        except Exception:
            continue
