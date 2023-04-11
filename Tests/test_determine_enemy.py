from unittest import TestCase
from unittest.mock import patch
import io

from Modules.battle import determine_enemy


class Test(TestCase):
    @patch('random.randint', return_value=5)
    def test_random_level_one(self, _):
        enemy = determine_enemy(1)
        expected_enemy = {'Name': 'Hashbrowns',
                          'Description': 'The thought of hashbrowns fill your mind. From the satisfying '
                                         'crunch of the potatoes to the savory flavors of the potatoes'
                                         'your body craves for a rest to indulge in this fried '
                                         'delicacy.',
                          'Frustration': 0, 'Max Frustration': 22, 'Intelligence': 22, 'Speed': 4, "Self-Control": 3,
                          "Luck": 0, "Exp": 2}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', return_value=1)
    def test_another_random(self, _):
        enemy = determine_enemy(1)
        expected_enemy = {'Name': 'Chicken Sandwich',
                          'Description': 'On the table lies a delicious chicken sandwich. The '
                                         'crisp, juicy, and tender chicken strips lie between 2 '
                                         'slices of freshly baked bread. You can feel the '
                                         'growling in our stomach drawing you towards it...',
                          'Frustration': 0, 'Max Frustration': 20, 'Intelligence': 23, 'Speed': 6, "Self-Control": 3,
                          "Luck": 0, "Exp": 1}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', return_value=5)
    def test_random_level_two(self, _):
        enemy = determine_enemy(2)
        expected_enemy = {'Name': 'Hashbrowns',
                          'Description': 'The thought of hashbrowns fill your mind. From the satisfying '
                                         'crunch of the potatoes to the savory flavors of the potatoes'
                                         'your body craves for a rest to indulge in this fried '
                                         'delicacy.',
                          'Frustration': 0, 'Max Frustration': 24, 'Intelligence': 24, 'Speed': 5, "Self-Control": 4,
                          "Luck": 0, "Exp": 2}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', return_value=5)
    def test_random_level_three(self, _):
        enemy = determine_enemy(3)
        expected_enemy = {'Name': 'Hashbrowns',
                          'Description': 'The thought of hashbrowns fill your mind. From the satisfying '
                                         'crunch of the potatoes to the savory flavors of the potatoes'
                                         'your body craves for a rest to indulge in this fried '
                                         'delicacy.',
                          'Frustration': 0, 'Max Frustration': 26, 'Intelligence': 26, 'Speed': 5, "Self-Control": 4,
                          "Luck": 0, "Exp": 2}
        self.assertEqual(expected_enemy, enemy)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_description(self, mock_output, _):
        determine_enemy(1)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "On the table lies a delicious chicken sandwich. The crisp, juicy, and tender chicken " \
                          "strips lie between 2 slices of freshly baked bread. You can feel the growling in our " \
                          "stomach drawing you towards it...\n"
        self.assertEqual(expected_output, the_game_printed_this)

    def test_typeerror(self):
        with self.assertRaises(TypeError):
            determine_enemy('s')

    def test_valueerror(self):
        with self.assertRaises(ValueError):
            determine_enemy(0)