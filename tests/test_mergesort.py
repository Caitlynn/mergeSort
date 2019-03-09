from unittest import TestCase

from mergesort import merge_sort


class Tests(TestCase):
    def test_sorts_sorted_list(self):
        l = [1, 2, 3, 4]
        l = merge_sort(l)
        self.assertListEqual(l, [1, 2, 3, 4])

    def test_sorts_revere_list(self):
        l = [5, 4, 3, 2, 1, 0, -1]
        l = merge_sort(l)
        self.assertListEqual(l, [-1, 0, 1, 2, 3, 4, 5])

    def test_sorts_empty_list(self):
        l = []
        l = merge_sort(l)
        self.assertListEqual(l, [])
