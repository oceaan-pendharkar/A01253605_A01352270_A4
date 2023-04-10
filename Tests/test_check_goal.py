from unittest import TestCase
from character import check_goal


class Test(TestCase):
    def test_raises_type_character(self):
        with self.assertRaises(TypeError):
            check_goal([], ())

    def test_raises_type_board(self):
        with self.assertRaises(TypeError):
            check_goal({}, [])

    def test_raises_value_error(self):
        with self.assertRaises(ValueError):
            check_goal({"column": 0, "row": 0, "Fitness": 0}, ())

    def test_raises_type_value(self):
        with self.assertRaises(TypeError):
            check_goal({"column": '0', "row": 0, "Fitness": 0, "Name": "person"}, ())

