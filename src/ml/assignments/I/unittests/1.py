import unittest
from ..apis import calculate_entropy

class TestCalculateEntropyAPI(unittest.TestCase):

    def testcase_0(self):
        self.assertEqual(calculate_entropy([1,1,1,1]), 0)

    def testcase_1(self):
        self.assertEqual(calculate_entropy([1,1,0,0]), 1)

    def testcase_2(self):
        self.assertEqual(calculate_entropy([0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,4]), 15/8)
        
    def testcase_3(self):
        self.assertEqual(calculate_entropy([0,0,0,0,1,2,3,4]), 2)
        
if __name__ == '__main__':
    unittest.main()
