from unittest import TestCase
from unittest.mock import patch

from Modules.battle import luck_roll


class Test(TestCase):
    @patch('random.randint', return_value=2)
    def test_luck_typeerror(self, _):
        with self.assertRaises(TypeError):
            luck_roll(1.2, -2, 2, 0)

    @patch('random.randint', return_value=2)
    def test_lower_typeerror(self, _):
        with self.assertRaises(TypeError):
            luck_roll(1, 'a', 2, 0)

    @patch('random.randint', return_value=2)
    def test_upper_typeerror(self, _):
        with self.assertRaises(TypeError):
            luck_roll(1, -2, 5.2, 0)

    @patch('random.randint', return_value=2)
    def test_luck_multiplier_typeerror(self, _):
        with self.assertRaises(TypeError):
            luck_roll(1, -2, 5.2, 'a')

    @patch('random.randint', return_value=2)
    def test_upper_valueerror(self, _):
        with self.assertRaises(ValueError):
            luck_roll(1, -2, -3, 0)

    @patch('random.randint', return_value=2)
    def test_without_luck_multiplier(self, _):
        self.assertEqual(2, luck_roll(1, -2, 2, 0))

    @patch('random.randint', return_value=2)
    def test_with_luck_multiplier(self, _):
        self.assertEqual(3, luck_roll(2, -2, 2, 0.5))
