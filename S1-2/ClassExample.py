
class Point:
    def __init__(self, x, y):
        """
        Init method that initializes the point with x and y
        :param x: X coordinate value
        :param y: Y coordinate value
        """
        self.x = x
        self.y = y
        # In my own instance of x and y, I am storing the values of x and y


# add random point
import random
france = []
for i in range(1, 5):
    france.append(Point(random.randint(1,9), random.randint(1,9)))
for i in range(0,4):
    print(france[i].x, france[i].y)



