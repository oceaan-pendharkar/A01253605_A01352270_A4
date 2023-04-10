from unittest import TestCase
from Modules.board import make_board


class Test(TestCase):
    def test_make_square(self):
        self.assertEqual(((0, 4), (0, 4)), make_board(4, 4))

    def test_make_more_rows(self):
        self.assertEqual(((0, 30), (0, 4)), make_board(30, 4))

    def test_make_more_cols(self):
        self.assertEqual(((0, 4), (0, 30)), make_board(4, 30))

    def test_lower_bound(self):
        self.assertEqual(((0, 2), (0, 2)), make_board(2, 2))

    def test_raises_row(self):
        with self.assertRaises(ValueError):
            make_board(1, 2)

    def test_raises_col(self):
        with self.assertRaises(ValueError):
            make_board(2, 1)

    def test_raises_both(self):
        with self.assertRaises(ValueError):
            make_board(0, 0)

    def test_type(self):
        board = make_board(4, 4)
        self.assertEqual(type(board), tuple)
