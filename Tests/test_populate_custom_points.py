import io
from unittest import TestCase
from unittest.mock import patch

from character import populate_custom_points


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[2, 2, 2, 2, 2])
    def test_normal_case(self, _, mock_output):
        character = {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(),
                         "You have 8 points left to distribute between your attributes.\n"
                         "You have 6 points left to distribute between your attributes.\n"
                         "You have 4 points left to distribute between your attributes.\n"
                         "You have 2 points left to distribute between your attributes.\n"
                         "You've used all your points!\n"
                         "You have 0 points left to distribute between your attributes.\n")

        self.assertEqual(character, {'Fitness': 5,
                                      'Intelligence': 7,
                                      'Level': 1,
                                      'Luck': 7,
                                      'Max Frustration': 62,
                                      'Motivation': 12,
                                      'Name': 'Name',
                                      'Self-Control': 7,
                                      'Speed': 5,
                                      'alive': True,
                                      'column': 0,
                                      'goal achieved': False,
                                      'row': 0})

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1, 1, 1, 2, 2, 2, 1])
    def test_cycle(self, _, mock_output):
        character = {"Motivation": 2, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': 'Name', "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(),
                         "You have 9 points left to distribute between your attributes.\n"
                         "You have 8 points left to distribute between your attributes.\n"
                         "You have 7 points left to distribute between your attributes.\n"
                         "You have 5 points left to distribute between your attributes.\n"
                         "You have 3 points left to distribute between your attributes.\n"
                         "You have 1 points left to distribute between your attributes.\n"
                         "You've used all your points!\n"
                         "You have 0 points left to distribute between your attributes.\n")
        self.assertEqual(character, {'Fitness': 5,
                                     'Intelligence': 7,
                                     'Level': 1,
                                     'Luck': 7,
                                     'Max Frustration': 61,
                                     'Motivation': 4,
                                     'Name': 'Name',
                                     'Self-Control': 6,
                                     'Speed': 7,
                                     'alive': True,
                                     'column': 0,
                                     'goal achieved': False,
                                     'row': 0})

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[0, 10])
    def test_early_stop(self, _, mock_output):
        character = {"Motivation": 34, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': 'name', "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(), "You have 10 points left to distribute between your attributes.\n"
                                                 "You've used all your points!\n"
                                                 "You have 0 points left to distribute between your attributes.\n")
        self.assertEqual(character, {'Fitness': 5,
                                     'Intelligence': 5,
                                     'Level': 1,
                                     'Luck': 5,
                                     'Max Frustration': 70,
                                     'Motivation': 34,
                                     'Name': 'name',
                                     'Self-Control': 5,
                                     'Speed': 5,
                                     'alive': True,
                                     'column': 0,
                                     'goal achieved': False,
                                     'row': 0})

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[11])
    def test_reprimand(self, _, mock_output):
        character = {"Motivation": 22, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': 'Name', "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        populate_custom_points(character, 10)
        self.assertEqual(mock_output.getvalue(), "Woah there, that was more points than we said!! "
                                                 "\nSince you cheated, that's all the points you get for now. "
                                                 "\nAnd you can forget about getting points for the category you just "
                                                 "over-filled. "
                                                 "\nThat's not how operation COMPLETE ASSIGNMENT 4 works..."
                                                 "\nYou have -1 points left to distribute between your attributes.\n")
        self.assertEqual({"Motivation": 22, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                          "Speed": 5,
                          "Fitness": 5, 'Name': 'Name', "row": 0, "column": 0,
                          "Level": 1,
                          "alive": True, "goal achieved": False}, character)

    def test_type_character(self):
        with self.assertRaises(TypeError):
            populate_custom_points([], 20)

    def test_type_points(self):
        with self.assertRaises(TypeError):
            populate_custom_points({}, '20')
