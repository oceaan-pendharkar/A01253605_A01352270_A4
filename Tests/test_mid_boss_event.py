import io
from unittest import TestCase
from unittest.mock import patch

from Modules.end_game import mid_boss_event


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_statement(self, mock_output):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        mid_boss_event(character, boss)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You've finished making all the code for assignment 4! You bask in your achievement before " \
                          "a sinking realization dawns upon you.\nYou still have to unit test everything... The " \
                          "thought of the endless unit tests makes you more frustrated and makes Assignment 4 so " \
                          "much harder to complete.\nAssignment 4's stats have increased and your frustration " \
                          "increases by 50.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_stat_change(self):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Name": "Assignment 3", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        mid_boss_event(character, boss)
        expected_character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 10, "Max Frustration": 500,
                              'Intelligence': 100, 'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30,
                              'Luck': 45, "row": 85, "column": 85}
        expected_boss = {"Name": "Assignment 3", "Frustration": 0, "Max Frustration": 200, "Intelligence": 28,
                         "Speed": 33, "Self-Control": 15, "Luck": 0, 'Exp': 0}
        self.assertEqual([expected_character, expected_boss], [character, boss])

    def test_typeerror_character(self):
        character = 23
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        with self.assertRaises(TypeError):
            mid_boss_event(character, boss)

    def test_typeerror_enemy(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = 69
        with self.assertRaises(TypeError):
            mid_boss_event(character, boss)

    def test_keyerror_character(self):
        character = {'Name': 'Bob', 'Motivation': 100, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        with self.assertRaises(KeyError):
            mid_boss_event(character, boss)

    def test_keyerror_enemy(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200,
                "Self-Control": 15, "Luck": 0, 'Exp': 0}
        with self.assertRaises(KeyError):
            mid_boss_event(character, boss)
