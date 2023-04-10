import io
from unittest import TestCase
from unittest.mock import patch

from Modules.end_game import boss_win


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_statement(self, mock_output):
        character = {'Name': 'Bob', 'Motivation': 110, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 4, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        boss_win(character, boss)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Congratulations Bob! You've beaten Assignment 4 and have completed the game! Hopefully " \
                          "your instructor will give you a good mark for it? Please?\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_typeerror_character(self):
        character = 23
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        with self.assertRaises(TypeError):
            boss_win(character, boss)

    def test_typeerror_enemy(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = 69
        with self.assertRaises(TypeError):
            boss_win(character, boss)

    def test_keyerror_character(self):
        character = {'Motivation': 101, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        with self.assertRaises(KeyError):
            boss_win(character, boss)

    def test_keyerror_enemy(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 1, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        with self.assertRaises(KeyError):
            boss_win(character, boss)