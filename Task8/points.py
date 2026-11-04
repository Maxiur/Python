class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    # konstuktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # zwraca string "(x, y)"
    def __str__(self):
        return f"({self.x}, {self.y})"

    # zwraca string "Point(x, y)"
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # obsługa point1 == point2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # obsługa point1 != point2
    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # v1 * v2, iloczyn skalarny, zwraca liczbę
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # długość wektora
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, 2)
        self.zero = Point(0, 0)

    def test_str(self):
        self.assertEqual(str(self.p1), "(3, 4)")
        self.assertEqual(str(self.p2), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(3, 4)")
        self.assertEqual(repr(self.p2), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(self.p1 == Point(3, 4))
        self.assertFalse(self.p1 == self.p2)

    def test_ne(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != Point(3, 4))

    def test_add(self):
        result = self.p1 + self.p2
        self.assertEqual(result, Point(4, 6))

    def test_sub(self):
        result = self.p1 - self.p2
        self.assertEqual(result, Point(2, 2))

    def test_mul(self):
        # iloczyn skalarny: 3*1 + 4*2 = 11
        self.assertEqual(self.p1 * self.p2, 11)

    def test_cross(self):
        # iloczyn wektorowy: 3*2 - 4*1 = 2
        self.assertEqual(self.p1.cross(self.p2), 2)

    def test_length(self):
        self.assertEqual(self.p1.length(), 5.0)  # 3-4-5 trójkąt
        self.assertEqual(self.zero.length(), 0.0)

    def test_hash(self):
        points_set = {self.p1, Point(3, 4), self.p2}
        self.assertEqual(len(points_set), 2)  # p1 i Point(3,4) to ten sam punkt

if __name__ == '__main__':
    unittest.main()
