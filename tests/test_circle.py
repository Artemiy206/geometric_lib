import math
import unittest

from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        r = 5
        expected_area = math.pi * r * r
        result = area(r)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        r = 2
        expected_perimeter = 2 * math.pi * r
        result = perimeter(r)
        self.assertEqual(result, expected_perimeter)

    def test_zero_circle_area(self):
        r = 0
        expected_area = math.pi * r * r
        result = area(r)
        self.assertEqual(result, expected_area)

    def test_zero_circle_perimeter(self):
        r = 0
        expected_perimeter = 2 * math.pi * r
        result = perimeter(r)
        self.assertEqual(result, expected_perimeter)

    def test_negative_circle_area(self):
        r = -2
        expected_area = math.pi * r * r
        result = area(r)
        self.assertEqual(result, expected_area)

    def test_negative_circle_perimeter(self):
        r = -3
        expected_perimeter = 2 * math.pi * r
        result = perimeter(r)
        self.assertEqual(result, expected_perimeter)

    def test_invalid_circle_area(self):
        with self.assertRaises(TypeError):
            area("2")

    def test_invalid_circle_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter([2])


if __name__ == '__main__':
    unittest.main()
