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


class Vector:
    def __init__(self, i: float, j: float, k: float = 0):
        self.i = i
        self.j = j
        self.k = k

    def __repr__(self) -> str:
        return f"<types.Vector(i={self.i}, j={self.j}, z={self.z})>"

    def __str__(self) -> str:
        return f"<{self.i}, {self.j}, {self.k}>" if self.k else f"<{self.i}, {self.j}>"

    def __add__(self, __o: object):
        return Vector(i=self.i + __o.i, j=self.j + __o.j, k=self.k + __o.k)

    def scale(self, scalar: float):
        self.i *= scalar
        self.j *= scalar
        self.k *= scalar
