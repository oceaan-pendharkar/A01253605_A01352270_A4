import io
from unittest import TestCase
from unittest.mock import patch

from board import guessing_game


class Test(TestCase):
    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=[5, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_number(self, mock_output, _, __):
        self.assertEqual(guessing_game(3), (True, 2))
        self.assertEqual(mock_output.getvalue(), "Looks like you input a number outside the range [1, 3]. "
                                                 "Try again...\n")

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_false_lower_bound(self, mock_output, _, __):
        self.assertEqual(guessing_game(2), (False, 2))
        self.assertEqual(mock_output.getvalue(), "")

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=['nice', 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_value_error(self, mock_output, _, __):
        self.assertEqual(guessing_game(3), (False, 3))
        self.assertEqual(mock_output.getvalue(), "Looks like you entered something other than an integer "
                                                 "[1, 3]. Try again...\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=[2])
    def test_true(self, _, __, mock_output):
        self.assertEqual(guessing_game(3), (True, 2))
        self.assertEqual(mock_output.getvalue(), "")

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=[3])
    def test_false(self, _, __):
        self.assertEqual(guessing_game(3), (False, 2))

    @patch('random.randint', return_value=22)
    @patch('builtins.input', side_effect=[555, "nice", 22])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_loop(self, mock_output, _, __):
        self.assertEqual(guessing_game(23), (True, 22))
        self.assertEqual(mock_output.getvalue(), "Looks like you input a number outside the range [1, 23]. "
                                                 "Try again...\nLooks like you entered something other than an integer "
                                                 "[1, 23]. Try again...\n")
