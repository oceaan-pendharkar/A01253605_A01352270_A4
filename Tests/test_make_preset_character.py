from unittest import TestCase
from character import make_preset_character


class Test(TestCase):
    @patch('builtins.input', side_effect=['n'])

    def test_n(self):
        self.fail()
