import io
from unittest import TestCase
from unittest.mock import patch

from Modules.battle import battle


class Test(TestCase):
    @patch('random.randint', side_effect=[100, 0])
    def test_slower_takes_damage(self, _):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 6, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        battle(True, character, enemy, 6)
        expected_enemy = {'Name': 'Chicken', 'Frustration': 8, 'Max Frustration': 6, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 2, "Luck": 0, "Exp": 1}
        expected_character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        self.assertEqual([expected_enemy, expected_character], [enemy, character])

    @patch('random.randint', side_effect=[100, 0, 100, 0, 100, 0])
    def test_hit_back(self, _):
        character = {'Name': 'Caleb', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        battle(True, character, enemy, 12)
        expected_enemy = {'Name': 'Chicken', 'Frustration': 16, 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                          "Self-Control": 2, "Luck": 0, "Exp": 1}
        expected_character = {'Name': 'Caleb', 'Motivation': 100, 'Frustration': 16, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        self.assertEqual([expected_enemy, expected_character], [enemy, character])

    @patch('random.randint', side_effect=[100, 0])
    def test_typeerror_character(self, _):
        character = 23423
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            battle(True, character, enemy, 12)

    @patch('random.randint', side_effect=[100, 0])
    def test_typeerror_enemy(self, _):
        character = {'Name': 'Caleb', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = 'jkadsn'
        with self.assertRaises(TypeError):
            battle(True, character, enemy, 12)

    @patch('random.randint', side_effect=[100, 0])
    def test_typeerror_character_is_faster(self, _):
        character = {'Name': 'Caleb', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            battle(1, character, enemy, 12)

    @patch('random.randint', side_effect=[100, 0])
    def test_keyerror_character(self, _):
        character = {'Name': 'Caleb', 'Motivation': 100, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            battle(True, character, enemy, 12)

    @patch('random.randint', side_effect=[100, 0])
    def test_keyerror_enemy(self, _):
        character = {'Name': 'Caleb', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            battle(True, character, enemy, 12)

    @patch('random.randint', side_effect=[100, 0])
    def test_valueerror(self, _):
        character = {'Name': 'Caleb', 'Motivation': 101, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 5, "Level": 2, "Fitness": 29, "Max Frustration": 100}
        enemy = {'Name': 'Chicken', 'Max Frustration': 12, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 2, "Luck": 0, "Exp": 1}
        with self.assertRaises(ValueError):
            battle(True, character, enemy, -500)

