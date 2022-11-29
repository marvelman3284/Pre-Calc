import sympy as sp
from sympy import init_printing
from sympy.abc import x
from typing import Optional


def clean_equation(eq: str):
    """
    Return a sympified equation.

    Given a string turn it into a equation that is usable by sympy.

    Args:
        eq (str): the equation to be sympified

    Returns:
        Any: a sympify equation
    """

    if eq == "":
        eq = input("Enter an equation: ")

    try:
        return sp.sympify(eq)
    except ValueError:
        print("Incorrect syntax!")
        print(
            "Enter one side of the equation (set everything equal to 0) using x and y (eg: x**2 - y == x**2 = y)"
        )
        new_eq: str = input("Enter the equation with correct syntax: ")
        return clean_equation(new_eq)


def expand(eq: Optional[str] = ""):
    """
    Returns an expanded equation.

    Given (or inputted) an equation expand it into its largest form.

    Example:
        >>> expand("(x+3)*(x+4)")
        x**2 + 7*x + 12

    Args:
        eq (Optional[str]): a string equation

    Returns:
        an equation in its most expanded form
    """
    eq = clean_equation(eq)
    return eq.expand()


def solve_eq(eq: Optional[str] = "") -> list:
    """
    Return a set of solutions of a given equation (solves for x).

    Given (or inputted) an equation (in terms of X) find and return possible solutions for it.

    Example:
        >>> solve("x**2 - 16")
        [{x: -4}, {x: 4}]

    Args:
        eq (Optional[str]): a string equation

    Returns:
        list: a list of solutions
    """
    eq = clean_equation(eq)
    return sp.solve(eq, x, dict=True)
