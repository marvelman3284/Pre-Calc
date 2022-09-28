import math


def herons(side_a: float, side_b: float, side_c: float):
    semi_perimeter = (side_a + side_b + side_c) / 2
    return math.sqrt(
        (
            semi_perimeter
            * (semi_perimeter - side_a)
            * (semi_perimeter - side_b)
            * (semi_perimeter - side_c)
        )
    )


def law_of_sines(
    side_a: float, angle_a: float, side_b: float = None, angle_b: float = None
):
    if side_b and angle_b:
        return None
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
            3,
        )
    elif angle_b:
        return (
            side_a
            * math.degrees(math.sin(math.radians(angle_b)))
            / math.degrees(math.sin(math.radians(angle_a)))
        )


def law_of_cosines(
    side_a: float, side_b: float, side_c: float = None, angle_c: float = None
):
    pass
