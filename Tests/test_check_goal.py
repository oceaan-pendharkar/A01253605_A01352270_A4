"""
Oceaan Pendharkar A01253605
Martin Su A01352270
"""
import io
from unittest import TestCase
from unittest.mock import patch

from Modules.character import check_goal


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

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ready_response(self, mock_output):
        character = {"column": 4, "row": 4, "Fitness": 30, "Name": "person"}
        check_goal(character, ((0, 5), (0, 5)))
        self.assertEqual(mock_output.getvalue(), "Nice job, person. You've reached the final square and you're ready to"
                                                 " defeat the final boss!!!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_last_square_response(self, mock_output):
        character = {"column": 4, "row": 4, "Fitness": 20, "Name": "person"}
        check_goal(character, ((0, 5), (0, 5)))
        self.assertEqual(mock_output.getvalue(),
                         "Hey there, person, you've found the final square, but you aren't ready"
                         " to defeat the boss yet! Keep trucking...\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fitness_good_response(self, mock_output):
        character = {"column": 4, "row": 2, "Fitness": 30, "Name": "person"}
        check_goal(character, ((0, 5), (0, 5)))
        self.assertEqual(mock_output.getvalue(), "Alright, person. You've got enough fitness points to defeat the "
                                                 "final boss! Make your way to the final square for the final battle..."
                                                 "\n")
