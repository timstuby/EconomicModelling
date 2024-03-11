
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

    def __str__(self):
        """
        How to print this point?
        :return:
        """
        return f"({self.x},{self.y})"

    def __repr__(self):
        """
                How to print this point if in a list?
                :return:
                """
        return self.__str__()
    def distfromorigin(self):
        distsquared = (self.x)**2 + (self.y)**2
        dist = distsquared**0.5
        return dist
    def __gt__(self, other):
        my_size = self.distfromorigin()
        their_size = other.distfromorigin()
        return my_size > their_size
    def __eq__(self,other):
        """
        How to compare with ==?
        :param other: the other point instance
        :return:
        """
        return self.distfromorigin() == other.distfromorigin()


if __name__ == "__main__":
    # add random point
    import random
    france = []
    for i in range(0, 5):
        france.append(Point(random.randint(1,99), random.randint(1,99)))

    print(france) # iterates and calls point.__repr__

    for point in france:
        print(point.distfromorigin())

    a = Point(2, 3)
    b = Point(7, 9)
    print(a.distfromorigin()>b.distfromorigin())
    print(a>b)

    france.sort()
    print(f"Thy point with greatest distance from origin is: {france[-1]} and thou smallest point is: {france[0]}")