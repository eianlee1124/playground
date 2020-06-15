from algorithms.sort import (
        bubble_sort,
        insertion_sort
)

import unittest

class TestSuite(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual([2, 9, 12, 17, 20, 33], [2, 12, 9, 17, 33, 20])
        


if __name__ == "__main__":
    unittest.main()
