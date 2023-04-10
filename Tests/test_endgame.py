import io
from unittest import TestCase
from unittest.mock import patch

from Modules.end_game import endgame


class Test(TestCase):
    @patch('random.randint', side_effect=[100, 0, 100, 0, 100, 0, 100, 0, 100, 0])
    def test_alive(self, _):
        character = {'Name': 'Bob', 'Motivation': 101, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        endgame(character, True)
        expected_character = {'Name': 'Bob', 'Motivation': 101, 'Frustration': 30, "Max Frustration": 500,
                              'Intelligence': 100, 'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30,
                              'Luck': 45, "row": 85, "column": 85}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dead(self, mock_output):
        character = {'Name': 'Bobi', 'Motivation': 101, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        endgame(character, False)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You lost all your motivation to finish assignment 4 and you decided that it's not worth " \
                          "it. It's such a nice day out right now you might as well go and enjoy life. Like a " \
                          "normal person...\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_typeerror_character(self):
        character = 'This is not a dictionary'
        with self.assertRaises(TypeError):
            endgame(character, False)

    def test_keyerror_character(self):
        character = {'Name': 'Bob', "Max Frustration": 500, 'Intelligence': 100,
                     'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
        with self.assertRaises(KeyError):
            endgame(character, False)

#         alive, not alive, errors
