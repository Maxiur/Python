from math import gcd   # Py3


# frac1 + frac2
def add_frac(frac1: list, frac2: list):
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    g = gcd(abs(num), abs(den))
    return [num // g, den // g]

# frac1 - frac2
def sub_frac(frac1, frac2):
    return add_frac(frac1, [-frac2[0], frac2[1]])

# frac1 * frac2
def mul_frac(frac1, frac2):
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    g = gcd(abs(num), abs(den))
    return [num // g, den // g]

# frac1 / frac2
def div_frac(frac1, frac2):
    return mul_frac(frac1, [frac2[1], frac2[0]])

# bool, czy dodatni
def is_positive(frac):
    return (frac[0] > 0) and (frac[1] > 0) or (frac[0] < 0) and (frac[1] < 0)

# bool, typu [0, x]
def is_zero(frac):
    return frac[0] == 0

# -1 | 0 | +1
def cmp_frac(frac1, frac2):
    diff = sub_frac(frac1, frac2)
    if diff[0] == 0:
        return 0
    elif is_positive(diff):
        return 1
    else:
        return -1

# konwersja do float
def frac2float(frac):
    return frac[0] / frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [-1, 3]), [1, 6])
        self.assertEqual(add_frac([-1, 2], [-1, 3]), [-5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [-1, 3]), [5, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 4], [1, 3]), [1, 12])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 4], [1, 3]), [3, 4])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 2], [1, 1]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy`