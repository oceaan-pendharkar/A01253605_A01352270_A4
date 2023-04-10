from unittest import TestCase
from character import check_goal


class Test(TestCase):
    def test_raises_type_character(self):
        with self.assertRaises(TypeError):
            check_goal([], ())

    def test_raises_type_board(self):
        with self.assertRaises(TypeError):
            check_goal({}, [])
