# coding=utf-8

import HTMLTestRunner
import unittest
from lesson2.test_unit_case import *

def gen_report():
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    filename = "test_math_report.html"
    with open(filename, "w") as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title="test math func report",
            description="case result"
        )
        runner.run(suite)

if __name__ == '__main__':
    gen_report()