import unittest

from original_app import find_duplicates as original_find
from optimized_app import find_duplicates as optimized_find


class TestDuplicateFinder(unittest.TestCase):

    def test_same_result(self):
        numbers = list(range(100)) * 2

        original_result = sorted(original_find(numbers))
        optimized_result = sorted(optimized_find(numbers))

        self.assertEqual(original_result, optimized_result)

    def test_duplicate_count(self):
        numbers = list(range(100)) * 2

        result = optimized_find(numbers)

        self.assertEqual(len(result), 100)


if __name__ == "__main__":
    unittest.main()