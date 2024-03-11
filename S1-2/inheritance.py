
from ClassExample import Point

# a = Point(5,5)
# print(a)

class ColorPoint(Point):
    # This is a class that inherits from point
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color} {self.x}, {self.y}>"

# 5 random color points
import random
colors = ['red', 'green', 'blue', 'yellow', 'celadon', 'xanadu', 'azul']
colors_points = []
for _ in range(5):
    color_points = ColorPoint(random.randint(0, 255), random.randint(0, 255), random.choice(colors))
    colors_points.append(color_points)
print(colors_points)