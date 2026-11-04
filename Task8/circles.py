from points import Point
import math
import numpy as np

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    # "Circle(x, y, radius)"
    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    # pole powierzchni
    def area(self):
        return math.pi * self.radius ** 2

    # przesuniecie o (x, y)
    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

    # najmniejszy okrąg pokrywający oba
    def cover(self, other):
        # odleglosc miedzy srodkami okregow
        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        # zwraca miare euklidesowa
        distance_between_centers = math.hypot(dx, dy)

        # Case 1: self zawiera w sobie okrag other
        if distance_between_centers + other.radius <= self.radius:
            return Circle(self.pt.x, self.pt.y, self.radius)

        # Case 2: other zawiera w sobie self
        if distance_between_centers + self.radius <= other.radius:
            return Circle(other.pt.x, other.pt.y, other.radius)

        # Case 3 żaden nie zawiera drugiego - wyznaczamy nowy okrag
        new_radius = (distance_between_centers + self.radius + other.radius) / 2.0

        # Wektor jednostkowy kierunku od self.pt do other.pt:
        # Przesunięcie od środka self.pt o odległość (new_radius - self.radius)
        k = (new_radius - self.radius) / distance_between_centers
        new_x = self.pt.x + dx * k
        new_y = self.pt.y + dy * k

        return Circle(new_x, new_y, new_radius)

    @classmethod
    def from_points(self, points: tuple[Point, Point, Point]):
        # x₁² + y₁² + D·x₁ + E·y₁ + F = 0
        # x₂² + y₂² + D·x₂ + E·y₂ + F = 0
        # x₃² + y₃² + D·x₃ + E·y₃ + F = 0

        # przenosimy x^2 + y^2 na drugą stronę

        # D·x₁ + E·y₁ + F·1 = -(x₁² + y₁²)
        # D·x₂ + E·y₂ + F·1 = -(x₂² + y₂²)
        # D·x₃ + E·y₃ + F·1 = -(x₃² + y₃²)

        # ┌          ┐   ┌   ┐   ┌              ┐
        # │ x₁ y₁ 1  │   │ D │   │ -(x₁² + y₁²) │
        # │ x₂ y₂ 1  │ · │ E │ = │ -(x₂² + y₂²) │
        # │ x₃ y₃ 1  │   │ F │   │ -(x₃² + y₃²) │
        # └          ┘   └   ┘   └              ┘

        p1, p2, p3 = points

        A = np.array([
            [p1.x, p1.y, 1],
            [p2.x, p2.y, 1],
            [p3.x, p3.y, 1]
        ])

        b = np.array([
            -(p1.x**2 + p1.y**2),
            -(p2.x**2 + p2.y**2),
            -(p3.x**2 + p3.y**2)
        ])

        try:
            D, E, F = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            raise ValueError("Punkty są współliniowe, nie da się stworzyć okręgu")

        cx = -D / 2
        cy = -E / 2
        radius = math.sqrt(cx**2 + cy**2 - F)

        return Circle(cx, cy, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return self.radius * 2

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
