import unittest

from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        a = 2
        expected_area = a * a
        result = area(a)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        a = 3
        expected_perimeter = 4 * a
        result = perimeter(a)
        self.assertEqual(result, expected_perimeter)

    def test_zero_area(self):
        a = 0
        expected_area = a * a
        result = area(a)
        self.assertEqual(result, expected_area)

    def test_zero_perimeter(self):
        a = 0
        expected_perimeter = 4 * a
        result = perimeter(a)
        self.assertEqual(result, expected_perimeter)

    def test_negative_area(self):
        a = -2
        expected_area = a * a
        result = area(a)
        self.assertEqual(result, expected_area)

    def test_negative_perimeter(self):
        a = -4
        expected_perimeter = 4 * a
        result = perimeter(a)
        self.assertEqual(result, expected_perimeter)

    def test_invalid_area(self):
        with self.assertRaises(TypeError):
            area("a")

    def test_invalid_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == '__main__':
    unittest.main()
