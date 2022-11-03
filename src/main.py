import os
from typing import Any
from functools import reduce
from rich import print
import numpy as np
import math

import cmd
import operator

import trig
import helpers.graph as graph
import helpers.symplify as sy


class graphShell(cmd.Cmd):
    intro = "Welcome to the math shell, '?' to view a list of commands \n"
    prompt = "(math) >>> "

    def do_add(self, arg: Any):
        """
        Returns the sum of n numbers.

        Args:
            *args (int): the numbers to be added together

        Returns:
            int: the sum of *args
        """
        print(sum(parse(arg)))

    def do_subtract(self, arg: Any):
        """
        Returns the difference of n numbers.

        Args:
            *args (int): the numbers to be subtracted from each other

        Returns:
            int: the difference of *args
        """
        print(reduce(operator.sub, parse(arg)))

    def do_multiply(self, arg: Any):
        """
        Returns the product of n numbers.

        Args:
            *args (int): the numbers to be multiplied together

        Returns:
            int: the product of *args
        """
        print(reduce(operator.mul, parse(arg)))

    def do_divide(self, arg: Any):
        """
        Returns the quotient of n numbers.

        Args:
            *args (int): the numbers to be divided from together

        Returns:
            int: the product of *args
        """
        print(reduce(operator.truediv, parse(arg)))

    def do_area_of_triangle(self, arg: Any):
        print(trig.herons(*parse(arg)))

    def do_area_of_oblique_triangle(self, arg: Any):
        print(trig.area_of_oblique_triangle(*parse(arg)))

    def do_law_of_sines(self, arg: Any):
        print(trig.law_of_sines(*parse(arg)))

    def do_law_of_cosines(self, arg: Any):
        print(trig.law_of_cosines(*parse(arg)))

    def do_sin(self, arg: Any):
        print(np.sin(np.radians(*parse(arg))))

    def do_cos(self, arg: Any):
        print(np.cos(np.radians(*parse(arg))))

    def do_tan(self, arg: Any):
        print(np.tan(np.radians(*parse(arg))))

    def do_arcsin(self, arg: Any):
        print(np.arcsin(np.radians(*parse(arg))))

    def do_arccos(self, arg: Any):
        print(np.arccos(np.radians(*parse(arg))))

    def do_arctan(self, arg: Any):
        print(np.arctan(np.radians(*parse(arg))))

    def do_graph(self, arg: Any):
        if not arg:
            arg = input("Enter the equation: ")

        start = int(input("Enter the start for the range: "))
        stop = int(input("Enter the stop for the  range: "))
        num_points = [start, stop]

        graph.graph_eq(arg, num_points)

    def do_solve(self, arg: Any):
        if arg != "":
            print(sy.solve(arg))
        else:
            print(sy.solve())

    def do_expand(self, arg: Any):
        if arg != "":
            print(sy.expand(arg))
        else:
            print(sy.expand())

    # help functions
    def help_expand(self):
        print(sy.expand.__doc__)

    def help_solve(self):
        print(sy.solve.__doc__)

    def help_graph(self):
        print(graph.graph_eq.__doc__)

    def help_area_of_triangle(self):
        print(trig.herons.__doc__)

    def help_area_of_oblique_triangle(self):
        print(trig.area_of_oblique_triangle.__doc__)

    def help_law_of_cosines(self):
        print(trig.law_of_cosines.__doc__)

    def help_law_of_sines(self):
        print(trig.law_of_sines.__doc__)

    def help_sin(self):
        doc = (math.sin.__doc__).split()
        doc[7] = "degrees)"
        print(" ".join(doc))

    def help_cos(self):
        doc = (math.cos.__doc__).split()
        doc[7] = "degrees)"
        print(" ".join(doc))

    def help_tan(self):
        doc = (math.tan.__doc__).split()
        doc[7] = "degrees)"
        print(" ".join(doc))

    def help_arcsin(self):
        doc = (math.asin.__doc__).split()
        doc[7] = "degrees)"
        print(" ".join(doc))

    def help_arccos(self):
        doc = (math.acos.__doc__).split()
        doc[7] = "degrees)"
        print(" ".join(doc))

    def help_arctan(self):
        doc = (math.atan.__doc__).split()
        doc[7] = "degrees)"
        print(" ".join(doc))

    # system/helper function
    def do_clear(self, _: Any):
        """
        Clears the screen
        """
        os.system("cls" if os.name == "nt" else "clear")

    def do_exit(self, _: Any):
        """
        Quits the program
        """
        quit()


def parse(arg):
    return tuple(map(int, arg.split()))


if __name__ == "__main__":
    while True:
        try:
            graphShell().cmdloop()
        except Exception:
            continue
