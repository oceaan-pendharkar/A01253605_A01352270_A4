from unittest import TestCase
from unittest.mock import patch
import io

from Modules.battle import level_up


class Test(TestCase):
    @patch('builtins.input', side_effect=[10])
    def test_level_up(self, _):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        level_up(character)
        new_character = {'Name': 'Bob', 'Motivation': 110, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                         "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        self.assertEqual(new_character, character)

    @patch('builtins.input', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print(self, mock_output, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        level_up(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You have 10 to allocate to your stats. Possible stats to increase are Motivation, Max " \
                          "Frustration,Self-Control, Intelligence, Luck, and Speed. Please allocate your points. \n" \
                          "You've used all your points!\nYou have 0 points left to distribute between your " \
                          "attributes.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_typeerror(self):
        character = 1
        with self.assertRaises(TypeError):
            level_up(character)

    def test_keyerror(self):
        character = {'Name': 'Bobby', 'Motivation': 100}
        with self.assertRaises(KeyError):
            level_up(character)
