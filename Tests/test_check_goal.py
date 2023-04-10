from unittest import TestCase
from character import check_goal


class Test(TestCase):
    def test_raises_type(self):
        character = []
        with self.assertRaises(TypeError):
            check_goal(character)
