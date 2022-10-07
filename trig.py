import math
import turtle


# TODO: turtle visualization
def draw_triangle(
    side_a: float,
    side_b: float,
    side_c: float,
    angle_a: float,
    angle_c: float,
) -> None:

    t = turtle.Turtle()

    t.forward(side_a)
    t.right(angle_c)
    t.forward(side_b)
    t.right(angle_a)
    t.forward(side_c)


# area of a triangle
def herons(side_a: float, side_b: float, side_c: float):
    """Return the area of a triangle.

    Using heron's formula calculate the area of a triangle

    Args:
        side_1: a float side length
        side_2: a float side length
        side_3: a float side length

    Returns:
        The area of the triangle (float)
    """

    semi_perimeter = (side_a + side_b + side_c) / 2
    return round(
        math.sqrt(
            (
                semi_perimeter
                * (semi_perimeter - side_a)
                * (semi_perimeter - side_b)
                * (semi_perimeter - side_c)
            )
        ),
        2,
    )


def area_of_oblique_triangle(side_a: float, side_b: float, angle_c: float) -> float:
    """
    Given two sides and an angle find the area of a triangle
    """
    return round(((side_a * side_b) * (math.sin(math.radians(angle_c))) / 2), 2)


# law of sines and cosines
def law_of_sines(
    side_a: float, angle_a: float, side_b: float = None, angle_b: float = None
) -> float:
    """
    Given an angle, a side, and either a second angle or side return the missing angle or side using law of sines
    """
    if side_b and angle_b:
        return 0
    elif side_b:
        return round(
            math.degrees(
                math.asin(
                    math.radians(
                        (side_b * (math.degrees(math.sin(math.radians(angle_a)))))
                        / side_a
                    )
                )
            ),
            2,
        )
    elif angle_b:
        return round(
            side_a
            * math.degrees(math.sin(math.radians(angle_b)))
            / math.degrees(math.sin(math.radians(angle_a))),
            2,
        )


def law_of_cosines(
    side_a: float, side_b: float, side_c: float = None, angle_c: float = None
) -> float:
    """Given two sides and either a third side or an angle return either the missing side or angle"""
    if side_c:
        return round(
            math.degrees(
                math.acos(
                    (side_c ** 2 - side_a ** 2 - side_b ** 2) / (-2 * side_a * side_b)
                )
            ),
            2,
        )
    elif angle_c:
        return round(
            math.sqrt(
                (
                    (side_a ** 2)
                    + (side_b ** 2)
                    - 2 * side_a * side_b * math.cos(math.radians(angle_c))
                )
            ),
            2,
        )


# Angular and linear speed
def angular_speed(central_angle: float) -> float:
    """
    Given the central angle return the angular speed (in radians)
    """
    return central_angle * 2 * math.pi


def linear_speed(central_angle: float, radius: float) -> float:
    """
    Given the central angle and the radius return the linear speed (in radians)
    """
    return round(angular_speed(central_angle) * radius, 2)


def solve(
    side_a: float,
    angle_a: float = None,
    side_b: float = None,
    angle_b: float = None,
    side_c: float = None,
    angle_c: float = None,
):
    if side_a and side_b and side_c:
        angle_c = law_of_cosines(side_a, side_b, side_c)
        angle_b = law_of_sines(side_c, angle_c, side_b)
        angle_a = 180 - angle_b - angle_c
        #
        # if 180 - angle_b + angle_c < 180:
        #     angle_b_prime = 180 - angle_b
        #     angle_a_prime = 180 - angle_b_prime - angle_c
        #
        #     print(
        #         f"Ambigous case: angle a: {angle_a_prime}, angle_b: {angle_b_prime}, angle_c: {angle_c}"
        #     )

        return f"angle a: {angle_a}, angle_b: {angle_b}, angle_c: {angle_c}"


# print(solve(side_a=318, side_b=206, side_c=193))
if __name__ == "__main__":
    pass
