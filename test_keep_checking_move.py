import io
from unittest import TestCase
from unittest.mock import patch

from board import keep_checking_move


class Test(TestCase):
    @patch('builtins.input', side_effect=['n'])
    def test_valid_north(self, _):
        self.assertEqual(keep_checking_move(((0, 5), (0, 5)), {"row": 2, "column": 1}), 'n')

    @patch('builtins.input', side_effect=['n', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_north(self, mock_output, _):
        keep_checking_move(((0, 5), (0, 5)), {"row": 0, "column": 1})
        self.assertEqual(mock_output.getvalue(), "Your move must stay within the bounds of the board!\n")

    @patch('builtins.input', side_effect=['s'])
    def test_valid_south(self, _):
        self.assertEqual(keep_checking_move(((0, 5), (0, 5)), {"row": 2, "column": 1}), 's')

    @patch('builtins.input', side_effect=['e'])
    def test_valid_east(self, _):
        self.assertEqual(keep_checking_move(((0, 5), (0, 5)), {"row": 2, "column": 1}), 'e')

    @patch('builtins.input', side_effect=['w'])
    def test_valid_west(self, _):
        self.assertEqual(keep_checking_move(((0, 5), (0, 5)), {"row": 2, "column": 1}), 'w')

    @patch('builtins.input', side_effect=['2', 'n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_value_error_output(self, mock_output, _):
        keep_checking_move(((0, 5), (0, 5)), {"row": 2, "column": 1})
        self.assertEqual(mock_output.getvalue(), "Direction must be 'n', 's', 'e', or 'w'!\n")

    @patch('builtins.input', side_effect=['2', 'i', '9', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_loops(self, mock_output, _):
        self.assertEqual(keep_checking_move(((0, 5), (0, 5)), {"row": 2, "column": 1}), 's')
        self.assertEqual(mock_output.getvalue(), "Direction must be 'n', 's', 'e', or 'w'!\nDirection must be 'n', "
                                                 "'s', 'e', or 'w'!\nDirection must be 'n', 's', 'e', or 'w'!\n")
