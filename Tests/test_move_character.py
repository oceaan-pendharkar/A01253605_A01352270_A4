"""
Oceaan Pendharkar A01253605
Martin Siu A01352270
"""
from unittest import TestCase
from unittest.mock import patch

from Modules.board import move_character


class Test(TestCase):
    def test_raises_board(self):
        with self.assertRaises(TypeError):
            move_character([(0, 2), (0, 2)], {"Name": "Saucy"})

    def test_raises_character(self):
        with self.assertRaises(TypeError):
            move_character(((0, 2), (0, 2)), [{"Name": "Saucy"}])

    def test_raises_luck_key(self):
        with self.assertRaises(ValueError):
            move_character(((0, 2), (0, 2)), {"Name": "Saucy"})

    def test_raises_luck_value(self):
        with self.assertRaises(ValueError):
            move_character(((0, 2), (0, 2)), {"Name": "Saucy", "Luck": "zero"})

    def test_raises_row(self):
        with self.assertRaises(ValueError):
            move_character(((0, 2), (0, 2)), {"Name": "Saucy", "Luck": 0, "column": 0})

    def test_raises_column(self):
        with self.assertRaises(ValueError):
            move_character(((0, 2), (0, 2)), {"Name": "Saucy", "Luck": 0, "row": 0})

    def test_raises_type_row(self):
        with self.assertRaises(TypeError):
            move_character(((0, 2), (0, 2)), {"Name": "Saucy", "Luck": 0, "row": '0', "column": 0})

    def test_raises_type_column(self):
        with self.assertRaises(TypeError):
            move_character(((0, 2), (0, 2)), {"Name": "Saucy", "Luck": 0, "row": 0, "column": '0'})

    @patch('builtins.input', side_effect=['s'])
    def test_south(self, _):
        character = {"Name": "Saucy", "row": 0, "column": 0, "Luck": 20}
        move_character(((0, 2), (0, 2)), character)
        self.assertEqual(character["row"], 1)

    @patch('builtins.input', side_effect=['n'])
    def test_north(self, _):
        character = {"Name": "Saucy", "row": 5, "column": 0, "Luck": 20}
        move_character(((0, 6), (0, 6)), character)
        self.assertEqual(character["row"], 4)

    @patch('builtins.input', side_effect=['e'])
    def test_east(self, _):
        character = {"Name": "Saucy", "row": 5, "column": 0, "Luck": 20}
        move_character(((0, 6), (0, 6)), character)
        self.assertEqual(character["column"], 1)

    @patch('builtins.input', side_effect=['w'])
    def test_west(self, _):
        character = {"Name": "Saucy", "row": 5, "column": 3, "Luck": 20}
        move_character(((0, 6), (0, 6)), character)
        self.assertEqual(character["column"], 2)
