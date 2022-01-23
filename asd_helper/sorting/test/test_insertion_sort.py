
import unittest
from typing import List

from asd_helper.sorting.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_simple(self):
        arr: List[int] = [12, 11, 13, 5, 6]
        sorted_arr: List[int] = [5, 6, 11, 12, 13]
        self.assertEqual(insertion_sort(arr), sorted_arr)

if __name__ == '__main__':
    unittest.main()
