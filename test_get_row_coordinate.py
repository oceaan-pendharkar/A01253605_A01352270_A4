from unittest import TestCase
from board import get_row_coordinate


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
