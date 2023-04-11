"""
Oceaan Pendharkar A01253605
Martin Siu A01352270
"""
from unittest import TestCase
from Modules.board import get_row_coordinate


class Test(TestCase):
    def test_south(self):
        character = {"row": 0, "column": 0}
        self.assertEqual(get_row_coordinate(character, 's'), 1)

    def test_negative_north(self):
        character = {"row": 0, "column": 0}
        self.assertEqual(get_row_coordinate(character, 'n'), -1)

    def test_big_south(self):
        character = {"row": 24, "column": 3}
        self.assertEqual(get_row_coordinate(character, 's'), 25)

    def test_big_north(self):
        character = {"row": 24, "column": 3}
        self.assertEqual(get_row_coordinate(character, 'n'), 23)

    def test_raises(self):
        character = {"row": 24, "column": 3}
        with self.assertRaises(ValueError):
            get_row_coordinate(character, 'j')

    def test_raises_N(self):
        character = {"row": 24, "column": 3}
        with self.assertRaises(ValueError):
            get_row_coordinate(character, 'N')

    def test_raises_row_key(self):
        character = {"column": 0}
        with self.assertRaises(KeyError):
            get_row_coordinate(character, 's')

    def test_type_character(self):
        character = []
        with self.assertRaises(TypeError):
            get_row_coordinate(character, 's')

    def test_type_move(self):
        character = {}
        with self.assertRaises(TypeError):
            get_row_coordinate(character, 2)
