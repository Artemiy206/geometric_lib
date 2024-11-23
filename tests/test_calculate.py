import math
import unittest

from calculate import calc


class TestCircle(unittest.TestCase):

    def test_calc_circle_perimetr(self):
        fig = 'circle'
        func = 'perimetr'
        size = 4
        expected_perimetr = 2 * math.pi * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_perimetr)

    def test_calc_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = 5
        expected_area = math.pi * size * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_area)

    def test_zero_calc_circle_perimetr(self):
        fig = 'circle'
        func = 'perimetr'
        size = 0
        expected_perimetr = 2 * math.pi * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_perimetr)

    def test_zero_calc_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = 0
        expected_area = math.pi * size * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_area)

    def test_negative_calc_circle_perimetr(self):
        fig = 'circle'
        func = 'perimetr'
        size = -4
        expected_perimetr = 2 * math.pi * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_perimetr)

    def test_negative_calc_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = -5
        expected_area = math.pi * size * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_area)


class TestSquare(unittest.TestCase):

    def test_calc_square_perimetr(self):
        fig = 'square'
        func = 'perimetr'
        size = 3
        expected_perimetr = 4 * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_perimetr)

    def test_calc_square_area(self):
        fig = 'square'
        func = 'area'
        size = 5
        expected_area = size * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_area)

    def test_zero_calc_square_perimetr(self):
        fig = 'square'
        func = 'perimetr'
        size = 0
        expected_perimetr = 4 * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_perimetr)

    def test_zero_calc_square_area(self):
        fig = 'square'
        func = 'area'
        size = 0
        expected_area = size * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_area)

    def test_negative_calc_square_perimetr(self):
        fig = 'square'
        func = 'perimetr'
        size = -3
        expected_perimetr = 4 * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_perimetr)

    def test_negative_calc_square_area(self):
        fig = 'square'
        func = 'area'
        size = -5
        expected_area = size * size
        result = calc(fig, func, size)
        self.assertEqual(result, expected_area)


if __name__ == '__main__':
    unittest.main()
