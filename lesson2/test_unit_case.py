import unittest
from unittest import skip
from lesson2.mathfunc import *

class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有用例执行前所执行的")

    def setUp(self):
        print("每个用例执行前所执行的")

    @skip("跳过不执行")
    def test_add(self):
        # 以test开头
        # self.assertEqual(add(1, 1), 3, "not equal")
        # self.assertEqual(add(10, 29), 39)
        # self.assertGreaterEqual(add(1,2), 3)
        self.assertLessEqual(add(2, 2), 6, "not less equal")

    @unittest.skip("临时跳过不执行")
    def test_minus(self):
        self.assertEqual(minus(10, 3), 7)
        self.assertEqual(minus(3, 9), -6)

    def test_multi(self):
        self.assertEqual(multi(3, 8), 24)
        self.assertEqual(multi(6, 7), 42)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(9, 3), 3)

    def tearDown(self):
        print("每个用例执行完后所执行的")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行完后所执行的")


if __name__ == '__main__':
    # verbosity指执行结果输出详细程度，0=简单， 1=一般， 2=详细
    unittest.main(verbosity=2)