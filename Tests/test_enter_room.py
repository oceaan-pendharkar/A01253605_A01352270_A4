import io
from unittest import TestCase
from unittest.mock import patch

from board import enter_room


class Test(TestCase):
    # test second condition: 'have to fight'
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2, 2, 2, -2, 2, 2, 0, 2, 0, 2, 2])  # all the calls to random.randint()
    @patch('builtins.input', side_effect=[2])  # input for guessing game
    def test_fight_correct(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(), "You're in McDonald's. There is a 1/2 chance you will have to fight if"
                                                 " you enter one of the listed numbers.\nYou KNEW this would happen! "
                                                 "You have to fight.\nYou can see a donut on display by the front "
                                                 "counter. The glaze on top of the donut glistens in the light, "
                                                 "tempting you towards its sweetness.\nYou have higher speed and "
                                                 "attack first\nOceaan landed a critical hit!\nYou frustrated Donut by "
                                                 "15.0 points\nYou won the battle!\nYou've gained 2 fitness points from"
                                                 " defeating Donut\nYou are now leaving McDonald's.\nHere's what your "
                                                 "points and stats look like:\n{'Luck': 20, 'Intelligence': 10, "
                                                 "'Motivation': 10, 'Self-Control': 10, 'Level': 1, 'Speed': 10, "
                                                 "'Frustration': 0, 'Max Frustration': 80, 'Name': 'Oceaan', "
                                                 "'Fitness': 2}\n")
        self.assertEqual(character["Fitness"], 2)
        self.assertEqual(character["Frustration"], 0)

    # test second condition: 'have to fight'
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2, 2, 2, -2, 2, 2, 0, 2, 0, 2, 2])  # all the calls to random.randint()
    @patch('builtins.input', side_effect=[1])  # input for guessing game
    def test_fight_incorrect(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(), "You're in McDonald's. There is a 1/2 chance you will have to fight "
                                                 "if you enter one of the listed numbers.\nThe number was 2.\nYou did "
                                                 "not have to fight. As you were...\nYou are now leaving "
                                                 "McDonald's.\nHere's what your points and stats look like:\n{'Luck': "
                                                 "20, 'Intelligence': 10, 'Motivation': 10, 'Self-Control': 10, "
                                                 "'Level': 1, 'Speed': 10, 'Frustration': 10, 'Max Frustration': 80, "
                                                 "'Name': 'Oceaan', 'Fitness': 0}\n")
        self.assertEqual(character["Fitness"], 0)
        self.assertEqual(character["Frustration"], 10)

    # test first condition: 'get assigned ANOTHER assignment', guessing correct value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[0, 2])
    @patch('builtins.input', side_effect=[2])
    def test_assignment_correct(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(), "You're in Some BCIT Classroom. There is a 1/3 chance you will get "
                                                 "assigned ANOTHER assignment if you enter one of the listed numbers."
                                                 "\nYou KNEW this would happen! You get assigned "
                                                 "ANOTHER assignment.\nYou are now leaving Some BCIT Classroom.\n"
                                                 "Here's what your points and stats look like:\n{'Luck': 18, "
                                                 "'Intelligence': 15, 'Motivation': 10, 'Self-Control': 10, "
                                                 "'Level': 1, 'Speed': 10, 'Frustration': 10, 'Max Frustration': 80, "
                                                 "'Name': 'Oceaan', 'Fitness': 0}\n")
        self.assertEqual(character["Motivation"], 10)
        self.assertEqual(character["Luck"], 18)

    # test first condition: 'get assigned ANOTHER assignment', guessing incorrect value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[3, 2])
    @patch('builtins.input', side_effect=[1])
    def test_assignment_incorrect(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(), "You're in Home. There is a 1/3 chance you will get "
                                                 "assigned ANOTHER assignment if you enter one of the listed numbers."
                                                 "\nThe number was 2.\nYou did not get assigned ANOTHER assignment. "
                                                 "As you were...\nYou are now leaving Home.\nHere's "
                                                 "what your points and stats look like:\n{'Luck': 20, 'Intelligence': "
                                                 "10, 'Motivation': 10, 'Self-Control': 10, 'Level': 1, 'Speed': 10, "
                                                 "'Frustration': 10, 'Max Frustration': 80, 'Name': 'Oceaan', 'Fitness'"
                                                 ": 0}\n")
        self.assertEqual(character["Motivation"], 10)
        self.assertEqual(character["Luck"], 20)

    # test third condition: 'lose self-control', guessing correct value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[6, 2])
    @patch('builtins.input', side_effect=[2])
    def test_self_control_correct(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(),
                         "You're in Pacific Centre. There is a 1/3 chance you will lose self-control if you enter one "
                         "of the listed numbers.\nYou KNEW this would happen! You lose self-control.\nYou are now "
                         "leaving Pacific Centre.\nHere's what your points and stats look like:\n{'Luck': 20, "
                         "'Intelligence': 10, 'Motivation': 10, 'Self-Control': 8, 'Level': 1, 'Speed': 10, "
                         "'Frustration': 10, 'Max Frustration': 80, 'Name': 'Oceaan', 'Fitness': 0}\n")
        self.assertEqual(character["Self-Control"], 8)

    # test third condition: 'lose self-control', guessing incorrect value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[7, 2])
    @patch('builtins.input', side_effect=[3])
    def test_self_control_incorrect(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(),
                         "You're in Levels Nightclub. There is a 1/3 chance you will lose self-control if you enter "
                         "one of the listed numbers.\nThe number was 2.\nYou did not lose self-control. As you "
                         "were...\nYou are now leaving Levels Nightclub.\nHere's what your points and stats look "
                         "like:\n{'Luck': 20, 'Intelligence': 10, 'Motivation': 10, 'Self-Control': 10, 'Level': 1, "
                         "'Speed': 10, 'Frustration': 10, 'Max Frustration': 80, 'Name': 'Oceaan', 'Fitness': 0}\n")
        self.assertEqual(character["Self-Control"], 10)

    # test fourth condition: 'lose self-control', guessing incorrect value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[4, 2])
    @patch('builtins.input', side_effect=[3])
    def test_motivation_incorrect(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(),
                         "You're in Granville Station. There is a 1/3 chance you will gain motivation if you enter "
                         "one of the listed numbers.\nThe number was 2.\nYou did not gain motivation. As you "
                         "were...\nYou are now leaving Granville Station.\nHere's what your points and stats look "
                         "like:\n{'Luck': 20, 'Intelligence': 10, 'Motivation': 10, 'Self-Control': 10, 'Level': 1, "
                         "'Speed': 10, 'Frustration': 10, 'Max Frustration': 80, 'Name': 'Oceaan', 'Fitness': 0}\n")
        self.assertEqual(character["Motivation"], 10)

    # test fourth condition: 'lose self-control', guessing correct value
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[5, 2])
    @patch('builtins.input', side_effect=[2])
    def test_motivation_correct(self, _, __, mock_output):
        character = {"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1, "Speed": 10,
                     "Frustration": 10, "Max Frustration": 80, "Name": "Oceaan", "Fitness": 0}
        enter_room(character)
        self.assertEqual(mock_output.getvalue(),
                         "You're in Waterfront Station. There is a 1/3 chance you will gain motivation if you enter "
                         "one of the listed numbers.\nYou KNEW this would happen! You gain motivation.\nYou are now "
                         "leaving Waterfront Station.\nHere's what your points and stats look like:\n{"
                         "'Luck': 20, 'Intelligence': 10, 'Motivation': 20, 'Self-Control': 10, 'Level': 1, "
                         "'Speed': 10, 'Frustration': 10, 'Max Frustration': 80, 'Name': 'Oceaan', 'Fitness': 0}\n")
        self.assertEqual(character["Motivation"], 20)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[5, 2])
    @patch('builtins.input', side_effect=[2])
    def test_raise_value(self, _, __, ___):
        with self.assertRaises(ValueError):
            enter_room({"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1,
                        "Speed": 10, 'Name': 'Oceaan', 'Fitness': 0})

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[5, 2])
    @patch('builtins.input', side_effect=[2])
    def test_raise_type(self, _, __, ___):
        with self.assertRaises(TypeError):
            enter_room({"Luck": 20, "Intelligence": 10, "Motivation": 10, "Self-Control": 10, "Level": 1,
                        "Speed": 10, "Frustration": '10', "Max Frustration": 80, 'Name': 'Oceaan', 'Fitness': 0})
