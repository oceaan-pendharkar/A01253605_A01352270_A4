import io
from unittest import TestCase
from unittest.mock import patch

from Modules.battle import deal_damage


class Test(TestCase):
    @patch('random.randint', side_effect=[100, 0])
    def test_character_deal_negative_damage(self, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 1, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 100, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        expected_enemy = {'Name': 'Chicken', 'Frustration': 1, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 100, "Luck": 0, "Exp": 1}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', side_effect=[100, 0])
    def test_charcter_deal_zero_damage(self, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        expected_enemy = {'Name': 'Chicken', 'Frustration': 1, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 10, "Luck": 0, "Exp": 1}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', side_effect=[100, 0])
    def test_character_deal_one_damage(self, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 11, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        expected_enemy = {'Name': 'Chickens', 'Frustration': 1, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 10, "Luck": 0, "Exp": 1}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', side_effect=[100, 0])
    def test_character_deal_large_damage(self, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 100, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        expected_enemy = {'Name': 'Chickens', 'Frustration': 90, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 10, "Luck": 0, "Exp": 1}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', side_effect=[1, 0])
    def test_character_critical_hit(self, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 15, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        expected_enemy = {'Name': 'Chickens', 'Frustration': 22, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 10, "Luck": 0, "Exp": 1}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', side_effect=[1, 0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_critical_hit(self, mock_output, _):
        character = {'Name': 'Bobbi', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 15, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Bobbi landed a critical hit!\nYou frustrated Chickens by 22 points\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[100, 0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_no_critical_hit(self, mock_output, _):
        character = {'Name': 'Bobbi', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 15, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(True, character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You frustrated Chickens by 5 points\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[100, 0])
    def test_character_take_damage(self, _):
        character = {'Name': 'Zed', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 100, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(False, character, enemy)
        expected_character = {'Name': 'Zed', 'Motivation': 100, 'Frustration': 16, 'Intelligence': 100, 'Speed': 10,
                              'Luck': 5, "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        self.assertEqual(expected_character, character)

    @patch('random.randint', side_effect=[100, 0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_take_damage(self, mock_output, _):
        character = {'Name': 'Bo', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 15, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chickens', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 10, "Luck": 0, "Exp": 1}
        deal_damage(False, character, enemy)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Chickens frustrated you by 16 points\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[100, 0])
    def test_typeerror_character(self, _):
        character = 4.23
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            deal_damage(True, character, enemy)

    @patch('random.randint', side_effect=[100, 0])
    def test_typeerror_enemy(self, _):
        character = {'Name': 'Al', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = "akjkasdk"
        with self.assertRaises(TypeError):
            deal_damage(True, character, enemy)

    @patch('random.randint', side_effect=[100, 0])
    def test_keyerror_character(self, _):
        character = {'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 5, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            deal_damage(True, character, enemy)

    @patch('random.randint', side_effect=[100, 0])
    def test_keyerror_enemy(self, _):
        character = {'Motivation': 150, 'Frustration': 0, 'Intelligence': 10, 'Speed': 1, 'Luck': 5,
                     "Self-Control": 5, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Max Frustration': 18, 'Intelligence': 21,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            deal_damage(True, character, enemy)
