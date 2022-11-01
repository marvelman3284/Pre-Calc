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


class Vector:
    def __init__(self, i: float, j: float, k: float = 0):
        self.i = i
        self.j = j
        self.k = k

    def __repr__(self):
        return f"<{self.i}, {self.j}, {self.k}>" if self.k else f"<{self.i}, {self.j}>"

    def scale(self, scalar: float):
        self.i *= scalar
        self.j *= scalar
        self.k *= scalar
