class Point:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        if type(o) != Point: 
            return false

        return self.x == o.x and self.y == o.y and self.z == z


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
