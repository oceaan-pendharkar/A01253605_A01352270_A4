from unittest import TestCase
from board import get_column_coordinate


class Test(TestCase):
    def test_east(self):
        character = {"row": 0, "column": 0}
        self.assertEqual(get_column_coordinate(character, 'e'), 1)

    def test_negative_west(self):
        character = {"row": 0, "column": 0}
        self.assertEqual(get_column_coordinate(character, 'w'), -1)

    def test_big_east(self):
        character = {"row": 2, "column": 24}
        self.assertEqual(get_column_coordinate(character, 'e'), 25)

    def test_big_west(self):
        character = {"row": 2, "column": 33}
        self.assertEqual(get_column_coordinate(character, 'w'), 32)

    def test_raises(self):
        character = {"row": 24, "column": 3}
        with self.assertRaises(ValueError):
            get_column_coordinate(character, 'j')

    def test_raises_E(self):
        character = {"row": 24, "column": 3}
        with self.assertRaises(ValueError):
            get_column_coordinate(character, 'E')

    def test_type_character(self):
        character = []
        with self.assertRaises(TypeError):
            get_column_coordinate(character, 'e')

    def test_type_move(self):
        character = {}
        with self.assertRaises(TypeError):
            get_column_coordinate(character, 2)
