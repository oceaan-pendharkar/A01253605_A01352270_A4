from unittest import TestCase
from unittest.mock import patch
import io

from Modules.battle import check_first


class Test(TestCase):
    @patch('random.randint', return_value=2)
    def test_character_is_faster(self, _):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        self.assertTrue(check_first(character, enemy))

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_is_faster_print(self, mock_output, _):
        character = {'Name': 'Alfred', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        check_first(character, enemy)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "You have higher speed and attack first\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('random.randint', return_value=2)
    def test_character_is_slower(self, _):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 7,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        self.assertFalse(check_first(character, enemy))

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_is_slower_print(self, mock_output, _):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 7,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        check_first(character, enemy)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "Chickens has higher speed and attacks first\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @patch('random.randint', return_value=2)
    def test_typeerror_character(self, _):
        character = 1
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 7,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            check_first(character, enemy)

    @patch('random.randint', return_value=2)
    def test_typeerror_enemy(self, _):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = 2
        with self.assertRaises(TypeError):
            check_first(character, enemy)

    @patch('random.randint', return_value=2)
    def test_keyerror_character(self, _):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 7,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            check_first(character, enemy)

    @patch('random.randint', return_value=2)
    def test_keyerror_enemy(self, _):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            check_first(character, enemy)
