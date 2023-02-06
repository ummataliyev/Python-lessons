class Vector:
    def __init__(self, x: int, y: int):
        self.x  = x
        self.y = y


    def __str__(self):
        return f"Vector <{self.x}, {self.y}>"

    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(3, 2)
v2 = Vector(3, 2)
v3 = v1 + v2

print(v1==v2)
print((v3))