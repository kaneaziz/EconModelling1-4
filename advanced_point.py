from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    AdvancedPoint extends ColorPoint by adding color validation and utility methods
    for working with colored points in 2D space.
    """
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initializes an AdvancedPoint with x, y coordinates and a color.
        Raises TypeError if the color is not in the allowed COLORS list.
        """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Getter for the x-coordinate of the point.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate of the point.
        """
        self._x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate of the point.
        """
        return self._y

    @property
    def color(self):
        """
        Getter for the color of the point.
        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Class method to add a new valid color to the COLORS list.
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Static method to create an AdvancedPoint from a (x, y) tuple
        and optional color (defaults to 'red').
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Static method to compute the Euclidean distance between two AdvancedPoint instances.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Instance method to compute the Euclidean distance from this point to another AdvancedPoint.
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

# Example usage
AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "rojo")
print(p.x)
print(p)
print(p.distance_origin())
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))
