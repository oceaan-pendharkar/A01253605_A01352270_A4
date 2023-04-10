from unittest import TestCase
from unittest.mock import patch

from Modules.end_game import boss_fight


class Test(TestCase):
    @patch('random.randint', side_effect=[100, 0, 100, 0, 100, 0, 100, 0, 100, 0])
    def test_character_win(self, _):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss_fight(character)
        expected_character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 30, "Max Frustration": 500,
                              'Intelligence': 100, 'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30,
                              'Luck': 45, "row": 85, "column": 85}
        self.assertEqual(expected_character, character)

    @patch('random.randint', side_effect=[100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0])
    def test_character_lose(self, _):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 40, 'Intelligence': 25,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss_fight(character)
        expected_character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 40, "Max Frustration": 40,
                              'Intelligence': 25, 'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30,
                              'Luck': 45, "row": 85, "column": 85}
        self.assertEqual(expected_character, character)

    def test_typeerror_character(self):
        character = 'This is not a dictionary'
        with self.assertRaises(TypeError):
            boss_fight(character)

    def test_keyerror_character(self):
        character = {'Name': 'Bob', "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        with self.assertRaises(KeyError):
            boss_fight(character)

