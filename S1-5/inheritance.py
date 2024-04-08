
from ClassExample import Point

# a = Point(5,5)
# print(a)

class ColorPoint(Point):
    # This is a class that inherits from point
    COLORS = ['red', 'green', 'blue', 'yellow', 'celadon', 'xanadu', 'azul']
    def __init__(self, x, y, color):
        #self.x = x
        #self.y = y
        super().__init__(x, y)
        # ^ Gets from the Parent.
        # In this inherited version of the color point, whenever you instantiate
        # , you do exactly like in the point, and then on top of that add the color.
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f'Unsupported color. Allows colors {self.COLORS}.')

    @classmethod
    def add_extra_color(cls, color):
        cls.COLORS.append(color)

    def __str__(self):
        return f"<{self.color} {self.x}, {self.y}>"

if __name__ == '__main__':
    red_point= ColorPoint(10,10, "red")
    ColorPoint.add_extra_color("orange") # Added for the class
    orange_point = ColorPoint(20,20, "orange")
    yellow_point = ColorPoint(30,30, "yellow")
    print(red_point.COLORS)
    # print(f"Orange point: {orange_point} has dist to origin = {orange_point.distfromorigin()}") # Before it was a property
    print(f"Orange point: {orange_point} has dist to origin = {orange_point.distfromorigin}") # After it was a property



    """
    # 5 random color points
    import random
    
    colors_points = []
    for _ in range(5):
        color_points = ColorPoint(random.randint(0, 255), random.randint(0, 255), random.choice(colors))
        colors_points.append(color_points)
    print(colors_points)
    """
