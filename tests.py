import unittest
import main


class Test(unittest.TestCase):
    def test_less_than_ten(self):
        self.assertEqual(main.less_than_ten([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]), [1, 1, 2, 3, 5, 8])
        self.assertEqual(main.less_than_ten([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(main.less_than_ten([]), [])
        self.assertEqual(main.less_than_ten([11, 12, 13, 14]), [])

    def test_less_than_x(self):
        self.assertEqual(main.less_than_x([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 22), [1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(main.less_than_x([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3), [1, 2])
        self.assertEqual(main.less_than_x([], 5), [])
        self.assertEqual(main.less_than_x([11, 12, 13, 14], 40), [11, 12, 13, 14])

if __name__ == '__main__':
    unittest.main()
