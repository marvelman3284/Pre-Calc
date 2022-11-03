import numpy as np


class Point:
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

    def __len__(self) -> int:
        return 3 if self.z else 2

    def __repr__(self) -> str:
        return f"<types.Point(x={self.x}, y={self.y}, z={self.z})>"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})" if self.z else f"({self.x}, {self.y})"

    def __add__(self, __o: object):
        if type(__o) != Point:
            raise TypeError(
                f"unsupported operand type(s) for +:'{type(self)}' and '{type(__o)}"
            )
        return Point(x=self.x + __o.x, y=self.y + __o.y, z=self.z + __o.z)

    def __sub__(self, __o: object):
        if type(__o) != Point:
            raise TypeError(
                f"unsupported operand type(s) for -:'{type(self)}' and '{type(__o)}"
            )
        return Point(x=self.x - __o.x, y=self.y - __o.y, z=self.z - __o.z)


# TODO: __add__, __mul__ (dot/scale), __sub__, __truediv__
class Vector:
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

    def __add__(self, __o: object):
        if type(__o) != Point:
            raise TypeError(
                f"unsupported operand type(s) for +:'{type(self)}' and '{type(__o)}"
            )
        return Vector(i=self.i + __o.i, j=self.j + __o.j, k=self.k + __o.k)

    def __sub__(self, __o: object):
        if type(__o) != Vector:
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
        if type(__o) != Vector:
            raise TypeError(
                f"unsupported operand type(s) for dot product: '{type(self)}' and '{type(__o)}'"
            )
        return (self.i * __o.i) + (self.j * __o.j) + (self.k * __o.k)
