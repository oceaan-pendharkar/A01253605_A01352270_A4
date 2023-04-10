from unittest import TestCase
from unittest.mock import patch
import io

from Modules.battle import calculate_fitness


class Test(TestCase):
    def test_no_level_up(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 1, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        calculate_fitness(character, enemy)
        expected_character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 1, "Fitness": 2, "Max Frustration": 100}
        self.assertEqual(expected_character, character)

    @patch('builtins.input', side_effect=[10])
    def test_level_two(self, _):
        character = {'Name': 'Boba', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        calculate_fitness(character, enemy)
        expected_character = {'Name': 'Boba', 'Motivation': 110, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 2, "Fitness": 15, "Max Frustration": 100}
        self.assertEqual(expected_character, character)

    @patch('builtins.input', side_effect=[10])
    def test_level_three(self, _):
        character = {'Name': 'Boba', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwiches', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        calculate_fitness(character, enemy)
        expected_character = {'Name': 'Boba', 'Motivation': 110, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 3, "Fitness": 30, "Max Frustration": 100}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_one(self, mock_output):
        character = {'Name': 'Alfred', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 5, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        calculate_fitness(character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You won the battle!\nYou've gained 1 fitness points from defeating Chickens\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_two(self, mock_output, _):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chick', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        calculate_fitness(character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You won the battle!\nYou've gained 1 fitness points from defeating Chick\n" \
                          "Congratulations! You have reached level 2!\n" \
                          "You have 10 to allocate to your stats. Possible stats to increase are Motivation, " \
                          "Max Frustration,Self-Control, Intelligence, Luck, and Speed. " \
                          "Please allocate your points. \n" \
                          "You've used all your points!\n" \
                          "You have 0 points left to distribute between your attributes.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_three(self, mock_output, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        calculate_fitness(character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You won the battle!\nYou've gained 1 fitness points from defeating Chicken\n" \
                          "Congratulations! You've reached level 3! Go get that boss now.\n" \
                          "You have 10 to allocate to your stats. Possible stats to increase are Motivation, " \
                          "Max Frustration,Self-Control, Intelligence, Luck, and Speed. " \
                          "Please allocate your points. \n" \
                          "You've used all your points!\n" \
                          "You have 0 points left to distribute between your attributes.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_character_typeerror(self):
        character = [1, 2, 3]
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            calculate_fitness(character, enemy)

    def test_enemy_typeerror(self):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = 'ndjasnkfnaskln'
        with self.assertRaises(TypeError):
            calculate_fitness(character, enemy)

    def test_character_keyerror(self):
        character = {'Name': 'Bobby', 'Motivation': 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            calculate_fitness(character, enemy)

    def test_enemy_keyerror(self):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 1, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0}
        with self.assertRaises(KeyError):
            calculate_fitness(character, enemy)

