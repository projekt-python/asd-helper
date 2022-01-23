"""Testing insertion sort module."""
import unittest
from typing import List

from asd_helper.sorting.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """Test suite for insertion sort."""

    def test_simple(self):
        """Test simple sorting."""
        arr: List[int] = [12, 11, 13, 5, 6, 1, 2]
        sorted_arr: List[int] = [1, 2, 5, 6, 11, 12, 13]
        self.assertEqual(insertion_sort(arr), sorted_arr)

    def test_another_simple(self):
        """Test simple sorting."""
        arr: List[int] = [12, 11, 13, 5, 6, 1, 3]
        sorted_arr: List[int] = [1, 3, 5, 6, 11, 12, 13]
        self.assertEqual(insertion_sort(arr), sorted_arr)


if __name__ == '__main__':
    unittest.main()
