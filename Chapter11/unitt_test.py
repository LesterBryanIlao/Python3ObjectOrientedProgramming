import unittest


class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual("1", "1")


def average(seq):
    return sum(seq) / len(seq)


class TestAverage(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])

    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])


if __name__ == "__main__":
    unittest.main()
