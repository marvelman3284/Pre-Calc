import math
from typing import Optional
from rich import print

# area of a triangle
def herons(side_a: float, side_b: float, side_c: float) -> float:
    """
    Return the area of a triangle.

    Using heron's formula calculate the area of a triangle

    Args:
        side_1 (float): a side length
        side_2 (float): a side length
        side_3 (float): a side length

    Returns:
        float: The area of the triangle
    """

    semi_perimeter = (side_a + side_b + side_c) / 2
    math.sqrt(
        (
            semi_perimeter
            * (semi_perimeter - side_a)
            * (semi_perimeter - side_b)
            * (semi_perimeter - side_c)
        )
    )


def area_of_oblique_triangle(side_a: float, side_b: float, angle_c: float) -> float:
    """
    Returns the area of a triangle given two sides and an angle.

    Using the formula A = 0.5*A*B*sin(c) return the area of a triangle.

    Args:
        side_a (float): side length.
        side_b (float): a float side length.
        angle_c (flaot): angle measure (in degrees).

    Returns:
        float: The area of a triangle.
    """

    return (side_a * side_b) * (math.sin(math.radians(angle_c))) / 2


# law of sines and cosines
def law_of_sines(
    side_a: float,
    angle_a: float,
    side_b: Optional[float] = None,
    angle_b: Optional[float] = None,
) -> float:
    """
    Return a missing angle or side of a triangle using the law of sines.

    Using the law of sines (sin(a)/A = sin(b)/B) find either angle b or side B

    Args:
        side_a (float): a side length.
        angle_a (float): an angle measurement (in degrees)
        side_b (Optional[float]): a side length.
        angle_b (Optional[float]): an angle measurement (in degrees)

    Returns:
        float: A missing side or angle (measured in degrees)
    """

    if side_b and angle_b:
        return 0
    elif side_b:
        math.degrees(
            math.asin(
                math.radians(
                    (side_b * (math.degrees(math.sin(math.radians(angle_a))))) / side_a
                )
            )
        )
    elif angle_b:
        return (
            side_a
            * math.degrees(math.sin(math.radians(angle_b)))
            / math.degrees(math.sin(math.radians(angle_a))),
        )
    else:
        return 0


def law_of_cosines(
    side_a: float,
    side_b: float,
    side_c: Optional[float] = None,
    angle_c: Optional[float] = None,
) -> float:
    """
    Return a missing angle or side of a triangle using the law of cosines.

    Using the law of cosines (C^2 = A^2 + B^2 - 2AB * cos(c)) find either angle c or side C

    Args:
        side_a (float): a side length.
        side_b (float): a side length.
        side_c (Optional[float]): a side length.
        angle_c (Optional[float]): an angle measurement (in degrees)

    Returns:
        float: A missing side or angle (measured in degrees)
    """

    if side_c:
        return math.degrees(
            math.acos(
                (side_c ** 2 - side_a ** 2 - side_b ** 2) / (-2 * side_a * side_b)
            )
        )
    elif angle_c:
        return math.sqrt(
            (
                (side_a ** 2)
                + (side_b ** 2)
                - 2 * side_a * side_b * math.cos(math.radians(angle_c))
            )
        )
    else:
        return 0


# Angular and linear speed
def angular_speed(central_angle: float) -> float:
    """
    Return the angular speed (measured in radians)

    Using the formula angular speed = (2pi * theta) / time ( assumed to be 1) return the angular speed

    Args:
        central_angle (float): the central angle (measured in radians)
    Returns:
        float: the angular speed (measured in radians)
    """

    return central_angle * 2 * math.pi


def linear_speed(central_angle: float, radius: float) -> float:
    """
    Return the linear speed (measured in radians)

    Using the formula linear speed = (angular_speed * radius) / time (assumed to be 1) return the linear speed

    Args:
        central_angle (float): the central angle (measured in radians)
        radius (float): the radius
    Returns:
        float: the linear speed (measured in radians)
    """

    return round(angular_speed(central_angle) * radius, 2)


def solve(sides: list[float], angles: list[float]) -> dict:
    """
    Return a dictionary with the missing sides/angles of a triangle.

    Given a side, an angle, and either a second side or angle solve for the remaining sides/angles of a triangle

    Args:
        sides (list[float]): list of sides (order matters: [side_a, side_b, side_c])
        angles (list[float]): list of angles measured in degrees  (order matters: [angle_a, angle_b, angle_c])
    """

    triangle: dict[str, list[float]] = {
        "side_a": [],
        "side_b": [],
        "side_c": [],
        "angle_a": [],
        "angle_b": [],
        "angle_c": [],
    }

    if len(sides) == 2 and len(angles) == 1:  # ssa case (no bad words in math)
        # deal with triangle 1 first
        second_angle = law_of_sines(side_a=sides[0], side_b=sides[1], angle_a=angles[0])
        third_angle = 180 - angles[0] - second_angle

        if angles[0] + second_angle + third_angle > 180:
            print("Triangle cannot exist!")
            return {}

        third_side = law_of_sines(
            side_a=sides[0], angle_a=angles[0], angle_b=third_angle
        )

        # check for a second triangle:
        second_angle_prime = (
            180 - second_angle if (180 - second_angle) + angles[0] < 180 else 0
        )

        # triangle 1
        triangle["angle_a"].append(angles[0])
        triangle["angle_b"].append(second_angle)
        triangle["angle_c"].append(third_angle)
        triangle["side_a"].append(sides[0])
        triangle["side_b"].append(sides[1])
        triangle["side_c"].append(third_side)

        if second_angle_prime != 0:
            triangle["angle_b"].append(second_angle_prime)
            third_angle_prime = 180 - angles[0] - second_angle_prime

            triangle["angle_c"].append(third_angle_prime)
            triangle["side_c"].append(
                law_of_sines(
                    side_a=sides[0], angle_a=angles[0], angle_b=third_angle_prime
                )
            )

    elif len(angles) == 2 and len(sides) == 1:  # aas
        second_side = law_of_sines(
            side_a=sides[0], angle_a=angles[0], angle_b=angles[1]
        )

        third_angle = 180 - angles[0] - angles[1]

        third_side = law_of_sines(
            side_a=sides[0], angle_a=angles[0], angle_b=third_angle
        )

        triangle["side_a"].append(sides[0])
        triangle["side_b"].append(second_side)
        triangle["side_c"].append(third_side)
        triangle["angle_a"].append(angles[0])
        triangle["angle_b"].append(angles[1])
        triangle["angle_c"].append(third_angle)

    elif len(sides) == 3 and len(angles) == 0:  # sss
        first_angle = law_of_cosines(sides[0], sides[1], sides[2])
        second_angle = law_of_cosines(sides[1], sides[2], sides[0])
        third_angle = law_of_cosines(sides[2], sides[0], sides[1])

        triangle["side_a"].append(sides[0])
        triangle["side_b"].append(sides[1])
        triangle["side_c"].append(sides[2])
        triangle["angle_a"].append(first_angle)
        triangle["angle_b"].append(second_angle)
        triangle["angle_c"].append(third_angle)

    return triangle


if __name__ == "__main__":
    pass
