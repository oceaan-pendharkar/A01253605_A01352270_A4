import io
from unittest import TestCase
from unittest.mock import patch

from board import enter_room


class Test(TestCase):
    # test second condition: 'have to fight'

    # @patch('random.randint', return_value=2)
    # @patch('random.randint', return_value=2)
    # @patch('builtins.input', side_effect=[2])
    # def test_enter_room(self, _, __, ___):
    #     character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
    #                  "Frustration": 10, "Max Frustration": 80}
    #     enter_room(character)

    # test first condition: 'get assigned ANOTHER assignment', guessing correct value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[0, 2])
    @patch('builtins.input', side_effect=[2])
    def test_assignment_correct(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(), "You're in Some BCIT Classroom. There is a 1/3 chance you will get "
                                                 "assigned ANOTHER assignment if you enter one of the listed numbers."
                                                 "\nYou KNEW this would happen! You get assigned "
                                                 "ANOTHER assignment.\nYou are now leaving Some BCIT Classroom.\n"
                                                 "Here's what your points and stats look like:\n{'Luck': 18, "
                                                 "'Intelligence': 15, 'Motivation': 10, 'Self-Control': 10, "
                                                 "'Level': 1, 'Speed': 10, 'Frustration': 10, 'Max Frustration': 80}\n")
        self.assertEqual(character["Motivation"], 10)
        self.assertEqual(character["Luck"], 18)

    # test first condition: 'get assigned ANOTHER assignment', guessing incorrect value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[3, 2])
    @patch('builtins.input', side_effect=[1])
    def test_assignment_incorrect(self, _, __,mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(), "You're in Home. There is a 1/3 chance you will get "
                                                 "assigned ANOTHER assignment if you enter one of the listed numbers."
                                                 "\nThe number was 2.\nYou did not get assigned ANOTHER assignment. "
                                                 "As you were...\nYou are now leaving Home.\nHere's "
                                                 "what your points and stats look like:\n{'Luck': 20, 'Intelligence': "
                                                 "10, 'Motivation': 10, 'Self-Control': 10, 'Level': 1, 'Speed': 10, "
                                                 "'Frustration': 10, 'Max Frustration': 80}\n")

        # test third condition: 'lose self-control', guessing correct value
        @patch('sys.stdout', new_callable=io.StringIO)
        @patch('random.randint', side_effect=[0, 2])
        @patch('builtins.input', side_effect=[1])
        def test_assignment_incorrect(self, _, __, mock_output):
            character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                         "Frustration": 10, "Max Frustration": 80}
            enter_room(character)
            self.assertEqual(mock_output.getvalue(),
                             "You're in Some BCIT Classroom. There is a 1/3 chance you will get "
                             "assigned ANOTHER assignment if you enter one of the listed numbers."
                             "\nThe number was 2.\nYou did not get assigned ANOTHER assignment. "
                             "As you were...\nYou are now leaving Some BCIT Classroom.\nHere's "
                             "what your points and stats look like:\n{'Luck': 20, 'Intelligence': "
                             "10, 'Motivation': 10, 'Self-Control': 10, 'Level': 1, 'Speed': 10, "
                             "'Frustration': 10, 'Max Frustration': 80}\n")
