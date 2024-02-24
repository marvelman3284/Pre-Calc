import numpy as np


class Point:
    """A point in 2-D or 3-D space"""

    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, __o: object) -> bool:
        if type(__o) != Point:
            return False

        return self.x == __o.x and self.y == __o.y and self.z == __o.z

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, Point):
            raise TypeError(f"'<' not supported between instances of 'Point' and '{type(__o)}'")
        return self.x < __o.x and self.y < __o.y

    def __len__(self) -> int:
        return 3 if self.z else 2

    def __repr__(self) -> str:
        return f"<types.Point(x={self.x}, y={self.y}, z={self.z})>"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})" if self.z else f"({self.x}, {self.y})"

    def __add__(self, __o: object):
        if not isinstance(__o, Point):
            raise TypeError(
                f"unsupported operand type(s) for +:'{type(self)}' and '{type(__o)}"
            )
        return Point(x=self.x + __o.x, y=self.y + __o.y, z=self.z + __o.z)

    def __sub__(self, __o: object):
        if not isinstance(__o, Point):
            raise TypeError(
                f"unsupported operand type(s) for -:'{type(self)}' and '{type(__o)}"
            )
        return Point(x=self.x - __o.x, y=self.y - __o.y, z=self.z - __o.z)


# TODO: __mul__ (dot/scale), __sub__, __truediv__
class Vector:
    """A vector in 2-D or 3-D space"""

    def __init__(self, i: float, j: float, k: float = 0):
        self.i = i
        self.j = j
        self.k = k

    def __repr__(self) -> str:
        return (
            f"<types.Vector(i={self.i}, j={self.j}, k={self.k})>"
            if self.k
            else f"<{self.i}, {self.j}>"
        )

    def __str__(self) -> str:
        return f"<{self.i}, {self.j}, {self.k}>" if self.k else f"<{self.i}, {self.j}>"

    def __eq__(self, __o: object) -> bool:
        return (
            (
                (self.i == __o.i and self.j == __o.j and self.k == __o.k)
                or (self.cross(__o) == Vector(0, 0, 0))
            )  # DOC: if the cross product of two vectors is a zero vector, then the two vectors are scalar multiples, so they must be equal
            if isinstance(__o, Vector)
            else False
        )

    def __add__(self, __o: object):
        if not isinstance(__o, Vector):
            raise TypeError(
                f"unsupported operand type(s) for +:'{type(self)}' and '{type(__o)}"
            )
        return Vector(i=self.i + __o.i, j=self.j + __o.j, k=self.k + __o.k)

    def __sub__(self, __o: object):
        if not isinstance(__o, Vector):
            raise TypeError(
                f"unsupported operand type(s) for -:'{type(self)}' and '{type(__o)}"
            )
        return Vector(i=self.i - __o.i, j=self.j - __o.j, k=self.k - __o.k)

    def magnitude(self) -> float:
        return np.sqrt(pow(self.i, 2) + pow(self.j, 2) + pow(self.k, 2))

    def unit_vector(self):
        return self.scale(1 / self.magnitude())

    def scale(self, scalar: float):
        return Vector(
            i=self.i * scalar,
            j=self.j * scalar,
            k=self.k * scalar,
        )

    def dot(self, __o: object) -> float:
        if not isinstance(__o, Vector):
            raise TypeError(
                f"unsupported operand type(s) for dot product: '{type(self)}' and '{type(__o)}'"
            )
        return (self.i * __o.i) + (self.j * __o.j) + (self.k * __o.k)

    def cross(self, __o: object):
        if not isinstance(__o, Vector):
            raise TypeError(
                f"unsupported operand type(s) for cross product: '{type(self)}' and '{type(__o)}'"
            )
        return Vector(
            i=(self.j * __o.k - self.k * __o.j),
            j=(self.k * __o.i - self.i * __o.k),
            k=(self.i * __o.j - self.j * __o.i),
        )

    def angle(self, __o: object):
        if not isinstance(__o, Vector):
            raise TypeError(
                f"unsupported operand type(s) for finding the angle: '{type(self)}' and '{type(__o)}'"
            )
        return round(
            np.arccos((self.dot(__o) / (self.magnitude() * __o.magnitude()))), 2
        )
