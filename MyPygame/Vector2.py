import math

class Vector2(object):
    """A vector!"""

    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY


    def __str__(self):
        return ("x: " + str(self.x) + "  y: " + str(self.y))


    def __add__(self, other):
        newVector = Vector2(self.x + other.x, self.y + other.y)
        return newVector


    def __sub__(self, other):
        newVector = Vector2(self.x - other.x, self.y - other.y)
        return newVector


    def dot (self, other):
        return (self.x * other.x + self.y * other.y)


    def scale(self, inputScale):
        newVector = Vector2(self.x * inputScale, self.y * inputScale)
        return newVector


    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)


    def normalized(self):
        myMagnitude = self.magnitude()
        if myMagnitude != 0:
            return Vector2(self.x * (1 / myMagnitude), self.y * (1 / myMagnitude))
            pass
        else:
            return Vector2(0, 0)