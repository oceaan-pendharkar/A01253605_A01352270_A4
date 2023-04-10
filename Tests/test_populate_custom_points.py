import io
from unittest import TestCase
from unittest.mock import patch

from character import populate_custom_points


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[0, 2, 2, 2, 2, 2])
    def test_normal_case(self, _, mock_output):
        character = {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': input("What's your character's name? "), "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(), "You have 10 points left to distribute between your attributes.\n"
                                                 "You have 8 points left to distribute between your attributes.\n"
                                                 "You have 6 points left to distribute between your attributes.\n"
                                                 "You have 4 points left to distribute between your attributes.\n"
                                                 "You have 2 points left to distribute between your attributes.\n"
                                                 "You've used all your points!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[0, 1, 1, 1, 2, 2, 2, 1])
    def test_cycle(self, _, mock_output):
        character = {"Motivation": 2, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': input("What's your character's name? "), "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(), "You have 10 points left to distribute between your attributes.\n"
                                                 "You have 9 points left to distribute between your attributes.\n"
                                                 "You have 8 points left to distribute between your attributes.\n"
                                                 "You have 7 points left to distribute between your attributes.\n"
                                                 "You have 5 points left to distribute between your attributes.\n"
                                                 "You have 3 points left to distribute between your attributes.\n"
                                                 "You have 1 points left to distribute between your attributes.\n"
                                                 "You've used all your points!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[0, 10])
    def test_early_stop(self, _, mock_output):
        character = {"Motivation": 34, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': input("What's your character's name? "), "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(), "You have 10 points left to distribute between your attributes.\n"
                                                 "You've used all your points!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[0, 11])
    def test_reprimand(self, _, mock_output):
        character = {"Motivation": 22, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': input("What's your character's name? "), "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(), "You have 10 points left to distribute between your attributes."
                                                 "\nWoah there, that was more points than we said!! "
                                                 "\nSince you cheated, that's all the points you get for now. "
                                                 "\nAnd you can forget about getting points for the category you just "
                                                 "over-filled. "
                                                 "\nThat's not how operation COMPLETE ASSIGNMENT 4 works...\n")
