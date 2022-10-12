import matplotlib.pyplot as plt
import numpy as np
from typing import Optional
import sympy as sp

# TODO: graphing functions


def graph(
    x: list[int],
    y: list[int],
    title: Optional[str] = None,
    x_ticks: Optional[str] = None,
    y_ticks: Optional[str] = None,
) -> None:
    ax = plt.subplot()
    plt.plot(x, y, marker='h')

    if title:
        plt.title(title)
    if x_ticks:
        ax.set_xticks(x_ticks)
    if y_ticks:
        ax.set_yticks(y_ticks)

    plt.show()


def clean_equations(eq: str):
    try:
        return sp.sympify(eq)
    except ValueError:
        print("Incorrect syntax!")
        new_eq: str = input("Enter the equation with correct syntax: ")
        return clean_equations(new_eq)


def graph_eq(eq: str, num_points: int):
    eq = clean_equations(eq)

    x = [i for i in range(num_points)]
    y = [eq.subs(sp.symbols("x"), i) for i in range(num_points)]  # type:ignore

    graph(x, y)


graph_eq("x**2", 5)
