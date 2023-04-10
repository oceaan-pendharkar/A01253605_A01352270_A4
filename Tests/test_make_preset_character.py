from unittest import TestCase
from unittest.mock import patch

from character import make_preset_character


class Test(TestCase):
    @patch('builtins.input', side_effect=['n'])
    def test_nerd(self, _):
        character = {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        make_preset_character(character)
        self.assertEqual(character,
                         {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 15, "Luck": 5,
                          "Speed": 5,
                          "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                          "alive": True, "goal achieved": False})

    @patch('builtins.input', side_effect=['l'])
    def test_leprechaun(self, _):
        character = {"Motivation": 10, "Max Frustration": 50, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        make_preset_character(character)
        self.assertEqual(character,
                         {"Motivation": 10, "Max Frustration": 50, "Self-Control": 5, "Intelligence": 5, "Luck": 15,
                          "Speed": 5,
                          "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                          "alive": True, "goal achieved": False})

    @patch('builtins.input', side_effect=['g'])
    def test_great_ape(self, _):
        character = {"Motivation": 10, "Max Frustration": 40, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        make_preset_character(character)
        self.assertEqual(character,
                         {"Motivation": 10, "Max Frustration": 40, "Self-Control": 15, "Intelligence": 5, "Luck": 5,
                          "Speed": 5,
                          "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                          "alive": True, "goal achieved": False})

    @patch('builtins.input', side_effect=['j'])
    def test_jock(self, _):
        character = {"Motivation": 10, "Max Frustration": 20, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                     "Speed": 5,
                     "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                     "alive": True, "goal achieved": False}
        make_preset_character(character)
        self.assertEqual(character,
                         {"Motivation": 10, "Max Frustration": 20, "Self-Control": 5, "Intelligence": 5, "Luck": 5,
                          "Speed": 15,
                          "Fitness": 5, 'Name': "Name", "row": 0, "column": 0, "Level": 1,
                          "alive": True, "goal achieved": False})
