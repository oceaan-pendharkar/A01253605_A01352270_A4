from unittest import TestCase
from board import move_character


class Test(TestCase):
    def test_raises_board(self):
        with self.assertRaises(TypeError):
            move_character([(0, 2), (0, 2)], {"Name": "Saucy"})

    def test_raises_character(self):
        with self.assertRaises(TypeError):
            move_character(((0, 2), (0, 2)), [{"Name": "Saucy"}])
