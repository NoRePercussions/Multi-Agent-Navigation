# Locations for navigation
# thshea 2021


from math import sin, cos
from math import ceil


class Location:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distanceTo(self, loc):
        return (self.x - loc.x)**2 \
             + (self.y - loc.y)**2

    def taxicabDistanceTo(self, loc):
        return abs(self.x - loc.x) \
             + abs(self.y - loc.y)

    def getLocationInDirection(self, dir, rad=1):
        return Location(
            self.x + rad*cos(dir),
            self.y + rad*sin(dir)
        )

    def getGridLocationInDirection(self, dir):
        return Location(
            self.x + ceil(cos(dir)),
            self.y + ceil(sin(dir))
        )
