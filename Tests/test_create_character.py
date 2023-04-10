import io
from unittest import TestCase
from unittest.mock import patch

from Modules.character import create_character


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Name", 'y', '10'])
    def test_create_custom(self, _, mock_output):
        self.assertEqual(create_character(), {"Motivation": 90, "Max Frustration": 60, "Self-Control": 5,
                                              "Intelligence": 5, "Luck": 5, "Speed": 5,
                                              "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                                              "alive": True, "goal achieved": False})
        self.assertEqual(mock_output.getvalue(), "Alright! Here are your base stats:"
                                                 "\n{'Motivation': 80, 'Max Frustration': 60, 'Self-Control': 5, "
                                                 "'Intelligence': 5, 'Luck': 5, 'Speed': 5, 'Fitness': 5, "
                                                 "'Name': 'Name', 'row': 0, 'column': 0, 'Level': 1, 'alive': True, "
                                                 "'goal achieved': False}"
                                                 "\nYou have ***10 points*** to distribute between Motivation, "
                                                 "Max Frustration, Self-Control, Intelligence, Luck, and Speed."
                                                 "\nMotivation: helps you stay alive"
                                                 "\nMax Frustration: the higher this is, the longer you last in battle"
                                                 "\nSelf-Control: like defense"
                                                 "\nIntelligence: helps you damage your enemies"
                                                 "\nLuck: determines how likely you are to meet difficult opponents"
                                                 "\nSpeed: helps you be quicker than your enemies!"
                                                 "\nYou also have Fitness, which keeps track of your experience level "
                                                 "(0 for now!).\nYou've used all your points!"
                                                 "\nYou have 0 points left to distribute between your attributes.\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Name", 'n', 'l'])
    def test_create_preset(self, _, mock_output):
        self.assertEqual(create_character(), {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5,
                                              "Intelligence": 5, "Luck": 15, "Speed": 5,
                                              "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                                              "alive": True, "goal achieved": False})
        self.assertEqual(mock_output.getvalue(), "")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Name", 2, 'n', 'l'])
    def test_wrong_input(self, _, mock_output):
        self.assertEqual(create_character(), {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5,
                                              "Intelligence": 5, "Luck": 15, "Speed": 5,
                                              "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                                              "alive": True, "goal achieved": False})
        self.assertEqual(mock_output.getvalue(), "You entered something other than 'y' or 'n'. Try again...\n")

    @patch('builtins.input', side_effect=["Name", 2, 'n', 'j'])
    def test_return_type(self, _):
        self.assertEqual(dict, type(create_character()))
