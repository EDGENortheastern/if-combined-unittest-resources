import unittest

class TestSmoke(unittest.TestCase):
    """Basic smoke tests using different unittest assertions."""

    def test_truth(self):
        # True should be True
        self.assertTrue(True)

    def test_falsehood(self):
        # False should be False
        self.assertFalse(False)

    def test_equal_numbers(self):
        # 2 + 2 should equal 4
        self.assertEqual(2 + 2, 4)

    def test_not_equal(self):
        # 5 should not equal 6
        self.assertNotEqual(5, 6)

    def test_almost_equal(self):
        # Values close within 3 decimal places should be almost equal
        self.assertAlmostEqual(3.1415, 3.1416, places=3)

    def test_not_almost_equal(self):
        # Values not close enough should not be almost equal
        self.assertNotAlmostEqual(3.1415, 3.15, places=2)

    def test_in(self):
        # 'a' should appear in 'cat'
        self.assertIn('a', 'cat')

    def test_not_in(self):
        # 'z' should not appear in 'cat'
        self.assertNotIn('z', 'cat')

    def test_is_none(self):
        # None should be None
        self.assertIsNone(None)

    def test_is_not_none(self):
        # A string is not None
        self.assertIsNotNone('hello')

    def test_greater(self):
        # 10 is greater than 5
        self.assertGreater(10, 5)

    def test_greater_equal(self):
        # 5 is greater than or equal to 5
        self.assertGreaterEqual(5, 5)

    def test_less(self):
        # 1 is less than 2
        self.assertLess(1, 2)

    def test_less_equal(self):
        # 3 is less than or equal to 3
        self.assertLessEqual(3, 3)

    def test_list_equal(self):
        # Two lists with the same elements in the same order are equal
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_dict_equal(self):
        # Two dictionaries with the same keys and values are equal
        self.assertDictEqual({'a': 1, 'b': 2}, {'a': 1, 'b': 2})

    def test_set_equal(self):
        # Two sets with the same items are equal regardless of order
        self.assertSetEqual({1, 2}, {2, 1})

    def test_tuple_equal(self):
        # Two identical tuples are equal
        self.assertTupleEqual((1, 2), (1, 2))

    def test_raises(self):
        # Division by zero should raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_count_equal(self):
        # Lists with the same elements, regardless of order or repetition, are equal in count
        self.assertCountEqual([1, 2, 2, 3], [3, 2, 1, 2])

if __name__ == '__main__':
    unittest.main()
