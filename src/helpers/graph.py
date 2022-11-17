import matplotlib.pyplot as plt
import numpy as np
from typing import Optional
import sympy as sp
from src.logic.geometry import Point, Vector


def scale(vec: Vector, scalar: float):
    return vec.scale(scalar)


def dot(v1: Vector, v2: Vector) -> int:
    return (v1.i * v2.i) + (v1.j * v2.j) + (v1.k * v2.k)


def distance(p1: Point, p2: Point) -> float:
    return np.sqrt(
        (np.pow(p2.x - p1.x, 2) + np.pow(p2.y - p1.y, 2) + np.pow(p2.z - p1.z, 2))
    )


# TODO: graphing functions


def graph(
    x: list[int],
    y: list[int],
    title: Optional[str] = None,
    x_ticks: Optional[list[str]] = None,
    y_ticks: Optional[list[str]] = None,
) -> None:
    """
    Graphs a set of (x, y) coordinates

    Args:
        x (list[int]): a list of all the x coordinates
        y (list[int]): a list of all the y coordinates
        title (Optional[str]): the title of the figure
        x_ticks (Optional[list[str]]): a list of strings to use as the x tick lables
        y_ticks (Optional[list[str]]): a list of strings to use as the y tick lables

    Returns:
        None
    """

    ax = plt.subplot()
    plt.plot(x, y, marker="h")

    if title:
        plt.title(title)
    if x_ticks:
        ax.set_xticklabels(x_ticks)
    if y_ticks:
        ax.set_yticklabels(y_ticks)

    plt.show()


def clean_equations(eq: str):
    """
    Return a sympified equation.

    Given a string turn it into a equation that is usable by sympy.

    Args:
        eq (str): the equation to be sympified

    Returns:
        Any: a sympify equation
    """

    try:
        return sp.sympify(eq)
    except ValueError:
        print("Incorrect syntax!")
        new_eq: str = input("Enter the equation with correct syntax: ")
        return clean_equations(new_eq)


def graph_eq(
    eq: str,
    num_points: list[int],
    title: Optional[str] = "Figure 1",
    x_ticks: Optional[list[str]] = None,
    y_ticks: Optional[list[str]] = None,
):
    """
    Graph an equation.

    Given an equation and an amount of points, graph the equation

    Args:
        eq (str): an equation, either passed into the function or collected as user input
        num_points (list[int]): a list containing the start and stop of the range, collected as user input
        title (Optional[str]): the title of the figure, defaults to "figure 1"
        x_ticks (Optional[list[str]]): a list of strings to use as the x tick lables, defaults to None
        y_ticks (Optional[list[str]]): a list of strings to use as the y tick lables, defaults to None

    Returns:
        None: prints a graph
    """

    eq = clean_equations(eq)

    x = [i for i in range(num_points[0], num_points[1] + 1)]
    y = [
        eq.subs(sp.symbols("x"), i) for i in range(num_points[0], num_points[1] + 1)  # type: ignore
    ]

    graph(x, y, title, x_ticks, y_ticks)
