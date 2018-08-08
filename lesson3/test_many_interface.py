# coding=utf-8

from lesson3.test_interface import TestInterfaceBaseFunc
import unittest

class TestMany(TestInterfaceBaseFunc):

    def __init__(self, *args, **kwargs):
        super(TestMany, self).__init__(*args, **kwargs)
        self.url = "http://www.jicheng.com"


if __name__ == '__main__':
    unittest.main(verbosity=2)