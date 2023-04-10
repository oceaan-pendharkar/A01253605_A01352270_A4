import io
from unittest import TestCase
from unittest.mock import patch

from character import check_goal


class Test(TestCase):
    def test_raises_type_character(self):
        with self.assertRaises(TypeError):
            check_goal([], ())

    def test_raises_type_board(self):
        with self.assertRaises(TypeError):
            check_goal({}, [])

    def test_raises_value_error(self):
        with self.assertRaises(ValueError):
            check_goal({"column": 0, "row": 0, "Fitness": 0}, ())

    def test_raises_type_value(self):
        with self.assertRaises(TypeError):
            check_goal({"column": '0', "row": 0, "Fitness": 0, "Name": "person"}, ())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_response(self, mock_output):
        character = {"column": 0, "row": 0, "Fitness": 0, "Name": "person"}
        check_goal(character, ((0, 5), (0, 5)))
        self.assertEqual(mock_output.getvalue(), "")

