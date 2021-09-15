import unittest
from ..apis import split 
import numpy as np

class TestSplitListWithRatioAPI(unittest.TestCase):

    @staticmethod
    def testcase_0():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,0], 10, 1),[[1],[2,3,4,5,6,7,8,9,0]] )

    @staticmethod
    def testcase_1():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,0], 10, 10),[[0],[1,2,3,4,5,6,7,8,9]] )

    @staticmethod
    def testcase_2():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,0], 10, 5),[[5],[1,2,3,4,6,7,8,9,0]] )
        
    @staticmethod
    def testcase_3():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,10,11,12], 10, 1),[[1],[2,3,4,5,6,7,8,9,10,11,12]] )

    @staticmethod
    def testcase_4():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,10,11,12], 10, 10),[[10,11,12],[1,2,3,4,5,6,7,8,9]] )
    
    @staticmethod
    def testcase_5():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,10,11,12], 10, 5),[[5],[1,2,3,4,6,7,8,9,10,11,12]] )
        
    @staticmethod
    def testcase_6():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 10, 1),[[1],[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]] )

    @staticmethod
    def testcase_7():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 10, 10),[[10,11,12,13,14,15,16],[1,2,3,4,5,6,7,8,9]] )
    
    @staticmethod
    def testcase_8():
        np.testing.assert_equal(split([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 10, 5),[[5],[1,2,3,4,6,7,8,9,10,11,12,13,14,15,16]] )
    
if __name__ == '__main__':
    unittest.main()
