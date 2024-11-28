import unittest

from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area(self):
        a = 5
        b = 2
        c = 3
        expected_area = (a + b + c) / 2
        result = area(a, b, c)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        a = 1
        b = 2
        c = 3
        expected_perimeter = a + b + c
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_zero_area(self):
        a = 0
        b = 0
        c = 0
        expected_area = (a + b + c) / 2
        result = area(a, b, c)
        self.assertEqual(result, expected_area)

    def test_zero_perimeter(self):
        a = 0
        b = 0
        c = 0
        expected_perimeter = a + b + c
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_negative_area(self):
        a = -1
        b = 2
        c = -5
        expected_area = (a + b + c) / 2
        result = area(a, b, c)
        self.assertEqual(result, expected_area)

    def test_negative_perimeter(self):
        a = -2
        b = 2
        c = -8
        expected_perimeter = a + b + c
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_invalid_inputs_area(self):
        with self.assertRaises(TypeError):
            area('a', 2, 3)

    def test_invalid_inputs_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 2, 3)


if __name__ == '__main__':
    unittest.main()
