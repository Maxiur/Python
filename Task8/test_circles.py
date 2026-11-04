import pytest
import math
from points import Point
from circles import Circle


class TestCircleBasic:
    """Testy podstawowych funkcjonalności klasy Circle"""

    def test_init(self):
        c = Circle(1, 2, 5)
        assert c.pt == Point(1, 2)
        assert c.radius == 5

    def test_init_negative_radius(self):
        with pytest.raises(ValueError, match="promień ujemny"):
            Circle(0, 0, -1)

    def test_repr(self):
        c = Circle(3, 4, 10)
        assert repr(c) == "Circle(3, 4, 10)"

    def test_eq(self):
        c1 = Circle(1, 2, 5)
        c2 = Circle(1, 2, 5)
        c3 = Circle(1, 2, 6)

        assert c1 == c2
        assert c1 != c3

    def test_area(self):
        c = Circle(0, 0, 3)
        assert math.isclose(c.area(), math.pi * 9)

        c_zero = Circle(1, 1, 0)
        assert c_zero.area() == 0

    def test_move(self):
        c = Circle(2, 3, 5)
        c.move(3, -1)
        assert c.pt == Point(5, 2)
        assert c.radius == 5


class TestCircleCover:
    """Testy metody cover"""

    def test_cover_concentric(self):
        c1 = Circle(0, 0, 3)
        c2 = Circle(0, 0, 5)
        cov = c1.cover(c2)
        assert cov.pt == Point(0, 0)
        assert cov.radius == 5

    def test_cover_one_contains_other(self):
        c1 = Circle(0, 0, 10)
        c2 = Circle(2, 0, 1)
        cov = c1.cover(c2)
        assert cov.pt == Point(0, 0)
        assert cov.radius == 10

class TestCircleFromPoints:
    """Testy metody klasowej from_points"""

    def test_from_points_simple_triangle(self):
        # Trójkąt prostokątny 3-4-5
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        p3 = Point(0, 4)

        circle = Circle.from_points((p1, p2, p3))

        # Środek okręgu opisanego na trójkącie prostokątnym
        # to środek przeciwprostokątnej
        assert math.isclose(circle.pt.x, 1.5, abs_tol=1e-9)
        assert math.isclose(circle.pt.y, 2.0, abs_tol=1e-9)
        assert math.isclose(circle.radius, 2.5, abs_tol=1e-9)

        # Sprawdzenie, że wszystkie punkty leżą na okręgu
        for p in [p1, p2, p3]:
            dist = math.hypot(p.x - circle.pt.x, p.y - circle.pt.y)
            assert math.isclose(dist, circle.radius, abs_tol=1e-9)

    def test_from_points_equilateral_triangle(self):
        # Trójkąt równoboczny o boku 2
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(1, math.sqrt(3))

        circle = Circle.from_points([p1, p2, p3])

        # Środek powinien być w (1, 1/sqrt(3))
        assert math.isclose(circle.pt.x, 1.0, abs_tol=1e-9)
        assert math.isclose(circle.pt.y, math.sqrt(3) / 3, abs_tol=1e-9)

        # Promień okręgu opisanego na trójkącie równobocznym o boku a: R = a/sqrt(3)
        expected_radius = 2 / math.sqrt(3)
        assert math.isclose(circle.radius, expected_radius, abs_tol=1e-9)

    def test_from_points_general_triangle(self):
        p1 = Point(1, 1)
        p2 = Point(4, 2)
        p3 = Point(3, 5)

        circle = Circle.from_points((p1, p2, p3))

        # Sprawdzenie, że wszystkie punkty leżą na okręgu
        for p in [p1, p2, p3]:
            dist = math.hypot(p.x - circle.pt.x, p.y - circle.pt.y)
            assert math.isclose(dist, circle.radius, abs_tol=1e-9)

class TestCircleBoundingBox:
    """Testy atrybutów wirtualnych (bounding box)"""

    def test_coordinates(self):
        c = Circle(5, 10, 3)

        assert c.top == 13
        assert c.bottom == 7
        assert c.left == 2
        assert c.right == 8

    def test_dimensions(self):
        c = Circle(5, 10, 3)

        assert c.width == 6
        assert c.height == 6

    def test_corners(self):
        c = Circle(5, 10, 3)

        assert c.topleft == Point(2, 13)
        assert c.topright == Point(8, 13)
        assert c.bottomleft == Point(2, 7)
        assert c.bottomright == Point(8, 7)

    def test_bounding_box_zero_radius(self):
        c = Circle(1, 2, 0)

        assert c.top == 2
        assert c.bottom == 2
        assert c.left == 1
        assert c.right == 1
        assert c.width == 0
        assert c.height == 0
        assert c.topleft == Point(1, 2)

    def test_properties_are_readonly(self):
        # Sprawdzenie, że atrybuty są tylko do odczytu
        c = Circle(0, 0, 5)

        with pytest.raises(AttributeError):
            c.top = 10

        with pytest.raises(AttributeError):
            c.topleft = Point(0, 0)


class TestCircleIntegration:
    """Testy integracyjne"""

    def test_from_points_and_bounding_box(self):
        # Utworzenie okręgu z punktów i sprawdzenie bounding box
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(2, 2)

        circle = Circle.from_points([p1, p2, p3])

        # Sprawdzenie, że bounding box zawiera wszystkie punkty
        for p in [p1, p2, p3]:
            assert circle.left <= p.x <= circle.right
            assert circle.bottom <= p.y <= circle.top

    def test_move_updates_bounding_box(self):
        c = Circle(0, 0, 5)
        original_topleft = c.topleft

        c.move(10, 20)

        assert c.topleft == Point(original_topleft.x + 10, original_topleft.y + 20)
        assert c.left == 5
        assert c.top == 25