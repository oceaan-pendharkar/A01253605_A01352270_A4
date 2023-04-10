from unittest import TestCase

from Modules.battle import check_result


def win_function(character, _):
    character['Name'] = 'win'


def lose_function(character, _):
    character['Name'] = 'lose'


class Test(TestCase):
    def test_battle_win(self):
        character = {'Name': 'C', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}

        expected_character = {'Name': 'win', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}

        check_result(character, enemy, lose_function, win_function)
        self.assertEqual(expected_character, character)

    def test_battle_lose(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 110, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandich', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}

        expected_character = {'Name': 'lose', 'Motivation': 100, 'Frustration': 110, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}

        check_result(character, enemy, lose_function, win_function)
        self.assertEqual(expected_character, character)

    def test_frustration_equal(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 100, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwichs', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}

        expected_character = {'Name': 'lose', 'Motivation': 100, 'Frustration': 100, 'Intelligence': 10, 'Speed': 10,
                              'Luck': 5, "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}

        check_result(character, enemy, lose_function, win_function)
        self.assertEqual(expected_character, character)

    def test_character_typeerror(self):
        character = 3
        enemy = {'Name': 'Chicken Sandwichs', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(TypeError):
            check_result(character, enemy, lose_function, win_function)

    def test_enemy_typeerror(self):
        character = {'Name': 'Bob', 'Motivation': 110, 'Frustration': 100, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = 2.616165151
        with self.assertRaises(TypeError):
            check_result(character, enemy, lose_function, win_function)

    def test_win_function_typeerror(self):
        character = {'Name': 'Bob', 'Motivation': 1110, 'Frustration': 100, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwichs', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 21}
        with self.assertRaises(TypeError):
            check_result(character, enemy, lose_function, 2)

    def test_lose_function_typeerror(self):
        character = {'Name': 'Bob', 'Motivation': 1111, 'Frustration': 100, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 100}
        enemy = {'Name': 'Chicken Sandwichs', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 21}
        with self.assertRaises(TypeError):
            check_result(character, enemy, 1, win_function)

    def test_character_keyerror(self):
        character = {'Intelligence': 10, 'Speed': 10, }
        enemy = {'Name': 'Chicken', 'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0, "Exp": 1}
        with self.assertRaises(KeyError):
            check_result(character, enemy, lose_function, win_function)

    def test_enemy_keyerror(self):
        character = {'Name': 'Bobby', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 10, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 1, "Max Frustration": 100}
        enemy = {'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5,
                 "Self-Control": 3, "Luck": 0}
        with self.assertRaises(KeyError):
            check_result(character, enemy, lose_function, win_function)
