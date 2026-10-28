from points import Point
import math

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

import unittest
class TestCircle(unittest.TestCase):

    def test_init(self):
        # Poprawna inicjalizacja
        c = Circle(1, 2, 5)
        self.assertEqual(c.pt, Point(1, 2))
        self.assertEqual(c.radius, 5)

        # Promień ujemny powinien wyrzucić ValueError
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_repr(self):
        c = Circle(3, 4, 10)
        self.assertEqual(repr(c), "Circle(3, 4, 10)")

    def test_eq_and_ne(self):
        c1 = Circle(1, 2, 5)
        c2 = Circle(1, 2, 5)
        c3 = Circle(1, 2, 6)
        c4 = Circle(0, 2, 5)

        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)
        self.assertNotEqual(c1, c4)

    def test_area(self):
        c = Circle(0, 0, 3)
        self.assertAlmostEqual(c.area(), math.pi * 9)

        # Okrąg o promieniu 0 ma pole 0
        c_zero = Circle(1, 1, 0)
        self.assertEqual(c_zero.area(), 0)

    def test_move(self):
        c = Circle(2, 3, 5)
        c.move(3, -1)
        self.assertEqual(c.pt, Point(5, 2))
        self.assertEqual(c.radius, 5)  # Promień się nie zmienia

    def test_cover(self):
        # 1. Okręgi współśrodkowe
        c1 = Circle(0, 0, 3)
        c2 = Circle(0, 0, 5)
        cov1 = c1.cover(c2)
        self.assertEqual(cov1.pt, Point(0, 0))
        self.assertEqual(cov1.radius, 5)

        # 2. Jednego okrąg zawiera się całkowicie w drugim (nie współśrodkowe)
        c3 = Circle(0, 0, 10)
        c4 = Circle(2, 0, 1)
        cov2 = c3.cover(c4)
        self.assertEqual(cov2.pt, Point(0, 0))
        self.assertEqual(cov2.radius, 10)

        # 3. Rozłączne okręgi na osi X
        c5 = Circle(0, 0, 2)
        c6 = Circle(10, 0, 3)
        cov3 = c5.cover(c6)
        # Odległość d = 10, d + r1 + r2 = 15 -> nowy promień = 7.5, środek w (2.5, 0)
        self.assertEqual(cov3.pt, Point(2.5, 0))
        self.assertEqual(cov3.radius, 7.5)


if __name__ == "__main__":
    unittest.main()
