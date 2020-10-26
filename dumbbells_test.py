import unittest

from dumbbells import weights_order


class DumbbellsTest(unittest.TestCase):
    def test_input(self):
        weights_list = weights_order([2.0, 1.0], 2)
        self.assertEqual(weights_list,
                         "Combinations are:\n"
                         "1.0\n"
                         "2.0\n"
                         "2.0 + 1.0 = 3.0")

    def test_my_setup(self):
        weights_list = weights_order([2.5, 2.0, 1.25, 0.5], 4)
        self.assertEqual(weights_list,
                         "Combinations are:\n"
                         "0.5\n"
                         "1.25\n"
                         "1.25 + 0.5 = 1.75\n"
                         "2.0\n"
                         "2.5\n"
                         "2.0 + 0.5 = 2.5\n"
                         "2.5 + 0.5 = 3.0\n"
                         "2.0 + 1.25 = 3.25\n")


if __name__ == "__main__":
    unittest.main()
