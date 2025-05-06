import random

class Point:
    """
    Point represents a point in 2D space with x and y coordinates.
    Includes methods for string representation, distance calculations,
    and comparisons based on distance from the origin.
    """
    def __init__(self, x, y):
        """
        Initialize a Point object.

        :param x: The x position on the axis (numeric).
        :param y: The y position on the axis (numeric).
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a human-readable string representation of the point.
        Format: <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Return the official string representation of the point.
        Uses the same format as __str__.
        """
        return self.__str__()

    def distance_origin(self):
        """
        Calculate the Euclidean distance from this point to the origin (0, 0).
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Compare two points based on their distance from the origin.
        Returns True if this point is farther than the other.

        :param other: Another Point instance.
        """
        my_distance = self.distance_origin()
        other_distance = other.distance_origin()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Compare two points based on their distance from the origin.
        Returns True if both points are equidistant.

        :param other: Another Point instance.
        """
        my_distance = self.distance_origin()
        other_distance = other.distance_origin()
        return my_distance == other_distance

# Example usage
p = Point(1, 2)  # p is an instance with coordinates (1, 2)
p2 = Point(2, 3)
p4 = Point(4.4, -55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x = 20
print(f"p.x={p.x} and p.y={p.y}")
print(p)

# Create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), random.randint(-10, 10)))

print("I got these 5 random points")
print(points)

p = Point(3, 4)
print(p.distance_origin())

p2 = Point(1, 1)
print(f"I am comparing p > p2: {p > p2}")

print("The sorted list of points is:")
points.sort()
print(points)