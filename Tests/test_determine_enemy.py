from unittest import TestCase
from unittest.mock import patch
import io

from battle import determine_enemy


class Test(TestCase):
    @patch('random.randint', return_value=5)
    def test_random_one(self):
        character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 3, 'Luck': 5,
                     "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 10}
        self.fail()

#     random one, random eight, random 5, TypeError, ValueError, print statement, dictionary copy, character level 1, character level 2
