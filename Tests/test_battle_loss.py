from unittest import TestCase
from unittest.mock import patch
import io

from Modules.battle import battle_loss


class Test(TestCase):
    def test_motivation_loss(self):
        character = {'Name': 'Bobs', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        battle_loss(character, enemy)
        expected_character = {'Name': 'Bobs', 'Motivation': 98, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_motivation_loss(self, mock_output):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        battle_loss(character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You gave in to the temptation of Chicken Sandwich! You lost 2 motivation.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_character_typeerror(self):
        character = [1, 2, 4]
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            battle_loss(character, enemy)

    def test_enemy_typeerror(self):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = 'hgvhlnlfrtdd'
        with self.assertRaises(TypeError):
            battle_loss(character, enemy)

    def test_character_keyerror(self):
        character = {'Name': 'Al', 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            battle_loss(character, enemy)

    def test_enemy_keyerror(self):
        character = {'Name': 'Bo', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 1, "Max Frustration": 100}
        enemy = {'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0}
        with self.assertRaises(KeyError):
            battle_loss(character, enemy)