from math import log2
import unittest
from ..apis import calculate_gain_ratio


class TestCalculateGainRatioAPI(unittest.TestCase):

    def testcase_0(self):
        self.assertEqual(calculate_gain_ratio(
            [1, 1, 1, 1], [[1, 1], [1, 1]]), 0)

    def testcase_1(self):
        self.assertEqual(calculate_gain_ratio(
            [1, 1, 0, 0], [[1, 1], [0, 0]]), 1)

    def testcase_2(self):
        self.assertAlmostEqual(calculate_gain_ratio(
            [0, 1, 1, 1], [[0, 1], [1, 1]]), 3/2-3/4*log2(3), 3)

    def testcase_3(self):
        self.assertAlmostEqual(calculate_gain_ratio(
            [0, 1, 1, 1], [[0], [1, 1, 1]]), (2-3/4*log2(3))/(-1/4*log2(1/4)-3/4*log2(3/4)), 3)

    def testcase_4(self):
        self.assertEqual(calculate_gain_ratio(
            [0, 1, 2, 3], [[0], [1, 2], [3]]), 1)


if __name__ == '__main__':
    unittest.main()
