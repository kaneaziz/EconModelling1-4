from point import Point
import random

class PointException(Exception):
    """
    Custom exception class for handling errors related to point operations.
    """
    pass

class ColorPoint(Point):
    """
    ColorPoint extends Point by adding a color attribute and validating
    that the x and y coordinates are numeric.
    """
    def __init__(self, x, y, color):
        """
        Initializes a ColorPoint with x, y coordinates and a color.
        Raises PointException if x or y is not a number (int or float).
        """
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")

        super().__init__(x, y)  # Initialize parent Point class
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the ColorPoint, showing its color and coordinates.
        """
        return f"<{self.color}: {self.x}, {self.y}>"

if __name__ == "__main__":
    # Example usage and testing of the ColorPoint class
    p = ColorPoint(1, 2, "red")
    print(p.distance_origin())
    print(p)
    # The following block was commented out; it generates random ColorPoints
    # and sorts them.
    # colors = ["red", "green", "blue", "yellow", "black", "magenta",
    #           "cyan", "white", "burgundy", "periwinkle", "marsala"]
    # color_points = []
    # for i in range(10):
    #     color_points.append(
    #         ColorPoint(random.randint(-10, 10),
    #                    random.randint(-10, 10),
    #                    random.choice(colors)))
    #
    # print(color_points)
    # color_points.sort()
    # print(color_points)