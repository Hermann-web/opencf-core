import unittest

from opencf_core.utils import ensure_iterable

class TestEnsureIterable(unittest.TestCase):
    def test_list(self):
        result = ensure_iterable([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_string(self):
        result = ensure_iterable("hello")
        self.assertEqual(result, "hello")

    def test_non_iterable(self):
        with self.assertRaises(TypeError):
            ensure_iterable(123, raise_err=True)

    def test_return_single(self):
        result = ensure_iterable(123, raise_err=False, return_single=True)
        self.assertEqual(result, (123,))

    def test_return_empty_tuple(self):
        result = ensure_iterable(123, raise_err=False)
        self.assertEqual(result, ())

if __name__ == '__main__':
    unittest.main()
