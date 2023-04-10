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
