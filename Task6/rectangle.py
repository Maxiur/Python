from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return f"Rectangle({self.pt1}, {self.pt2})"

    # obsługa rect1 == rect2
    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    # pole powierzchni
    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    # zakładam że przesuwany nie jak funkcje tylko jako punkt, dlatego +
    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Tworzenie prostokątów do testów
        self.rect1 = Rectangle(0, 0, 4, 3)
        self.rect2 = Rectangle(1, 1, 5, 4)
        self.rect3 = Rectangle(0, 0, 4, 3)  # identyczny jak rect1

    def test_init(self):
        # Sprawdzenie poprawności inicjalizacji
        self.assertEqual(self.rect1.pt1.x, 0)
        self.assertEqual(self.rect1.pt1.y, 0)
        self.assertEqual(self.rect1.pt2.x, 4)
        self.assertEqual(self.rect1.pt2.y, 3)

    def test_str(self):
        # Test metody __str__
        expected = "[(0, 0), (4, 3)]"
        self.assertEqual(str(self.rect1), expected)

    def test_repr(self):
        # Test metody __repr__
        expected = "Rectangle((0, 0), (4, 3))"
        self.assertEqual(repr(self.rect1), expected)

    def test_eq(self):
        # Test równości prostokątów
        self.assertEqual(self.rect1, self.rect3)
        self.assertNotEqual(self.rect1, self.rect2)

    def test_ne(self):
        # Test nierówności prostokątów
        self.assertTrue(self.rect1 != self.rect2)
        self.assertFalse(self.rect1 != self.rect3)

    def test_center(self):
        # Test obliczania środka prostokąta
        center = self.rect1.center()
        self.assertEqual(center.x, 2.0)
        self.assertEqual(center.y, 1.5)

        center2 = self.rect2.center()
        self.assertEqual(center2.x, 3.0)
        self.assertEqual(center2.y, 2.5)

    def test_area(self):
        # Test obliczania pola powierzchni
        self.assertEqual(self.rect1.area(), 12)  # 4 * 3
        self.assertEqual(self.rect2.area(), 12)  # 4 * 3

        rect_small = Rectangle(0, 0, 2, 2)
        self.assertEqual(rect_small.area(), 4)

    def test_move(self):
        # Test przesuwania prostokąta
        self.rect1.move(2, 3)
        self.assertEqual(self.rect1.pt1.x, 2)
        self.assertEqual(self.rect1.pt1.y, 3)
        self.assertEqual(self.rect1.pt2.x, 6)
        self.assertEqual(self.rect1.pt2.y, 6)

        # Sprawdzenie że środek też się przesunął
        center = self.rect1.center()
        self.assertEqual(center.x, 4.0)
        self.assertEqual(center.y, 4.5)


if __name__ == '__main__':
    unittest.main()
