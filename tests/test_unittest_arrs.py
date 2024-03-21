import unittest
from utils import arrs


class TesttArs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, 'test'), 2)
        self.assertEqual(arrs.get([], 0, 'test'), 'test')


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1 ), [2, 3])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([0, 0, 0], None, None), [0, 0, 0])
        #assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        #assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        #assert arrs.my_slice([], 0) == []
       # assert arrs.my_slice([0, 0, 0], None, None) == [0, 0, 0]

