import io
from unittest import TestCase
from unittest.mock import patch

from board import guessing_game


class Test(TestCase):
    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=['nice', 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_value_error(self, mock_output, _, __):
        guessing_game(3)
        self.assertEqual(mock_output.getvalue(), "Looks like you entered something other than an integer "
                                                 "[1, 3]. Try again...\n")
