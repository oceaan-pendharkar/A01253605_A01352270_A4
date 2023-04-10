import io
from unittest import TestCase
from unittest.mock import patch

from Modules.character import check_vitals


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dead(self, mock_output):
        character = {"Motivation": 0, "alive": True, "row": 5, "column": 8, "Fitness": 30, "Name": "Bob"}
        check_vitals(character, ((0, 9), (0, 9)))
        self.assertEqual(mock_output.getvalue(), "Sorry, you lost all your motivation... you're basically dead. Have "
                                                 "fun in the afterlife!\n")
        self.assertEqual(character["alive"], False)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fitness(self, mock_output):
        character = {"Motivation": 20, "alive": True, "row": 5, "column": 8, "Fitness": 30, "Name": "Bob"}
        check_vitals(character, ((0, 9), (0, 9)))
        self.assertEqual(mock_output.getvalue(), "Alright, Bob. You've got enough fitness points to defeat the final "
                                                 "boss! Make your way to the final square for the "
                                                 "final battle...\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_nothing(self, mock_output):
        character = {"Motivation": 20, "alive": True, "row": 5, "column": 8, "Fitness": 20, "Name": "Bob"}
        check_vitals(character, ((0, 9), (0, 9)))
        self.assertEqual(mock_output.getvalue(), "")
        self.assertEqual(character["alive"], True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_square(self, mock_output):
        character = {"Motivation": 20, "alive": True, "row": 8, "column": 8, "Fitness": 10, "Name": "Bob"}
        check_vitals(character, ((0, 9), (0, 9)))
        self.assertEqual(mock_output.getvalue(), "Hey there, Bob, you've found the final square, but you aren't ready "
                                                 "to defeat the boss yet! Keep trucking...\n")
        self.assertEqual(character["alive"], True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_goal_achieved(self, mock_output):
        character = {"Motivation": 20, "alive": True, "row": 8, "column": 8, "Fitness": 30, "Name": "Bob"}
        check_vitals(character, ((0, 9), (0, 9)))
        self.assertEqual(mock_output.getvalue(), "Nice job, Bob. You've reached the final square and you're ready to "
                                                 "defeat the final boss!!!\n")
        self.assertTrue(character["alive"])

    def test_raises_type_character(self):
        character = [{"Motivation": 20, "alive": True, "row": 8, "column": 8, "Fitness": 30, "Name": "Bob"}]
        with self.assertRaises(TypeError):
            check_vitals(character, ())

    def test_raises_type_board(self):
        with self.assertRaises(TypeError):
            check_vitals({}, [])

    def test_raises_value_key(self):
        character = {"Motivation": 20, "row": 8, "column": 8, "Fitness": 30, "Name": "Bob"}
        with self.assertRaises(ValueError):
            check_vitals(character, ())

    def test_raises_type_key(self):
        character = {"Motivation": 20, "alive": True, "row": '8', "column": 8, "Fitness": 30, "Name": "Bob"}
        with self.assertRaises(TypeError):
            check_vitals(character, ())
