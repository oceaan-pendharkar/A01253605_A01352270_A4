"""
Oceaan Pendharkar A01253605
Martin Su A01352270
"""
import io
from unittest import TestCase
from unittest.mock import patch

from Modules.board import initialize_game


class Test(TestCase):
    def test_return_values(self):
        self.assertEqual((((0, 2), (0, 2)), {"Name": "Tiny", "stats": 0}), initialize_game(((0, 2), (0, 2)),
                                                                                           {"Name": "Tiny",
                                                                                            "stats": 0}))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_welcome(self, mock_output):
        initialize_game(((0, 5), (0, 5)), {"Name": "Tiny", "stats": 0})
        self.assertEqual(mock_output.getvalue(), "Welcome to the game, Tiny! You are on MISSION: COMPLETE ASSIGNMENT 4."
                                                 "\nYou're at the end of your first term in CST and things have been "
                                                 "hectic as HECK.\nBut don't worry, we know you can do it!\nYour "
                                                 "mission is to stay Motivated enough to stay alive, achieve "
                                                 "enough Fitness level to defeat the final boss, and\nmake it to the "
                                                 "last square of the board for the final battle...\n")

    def test_raises_board(self):
        with self.assertRaises(TypeError):
            initialize_game([(0, 5), (0, 5)], {"Name": "Tiny", "stats": 0})

    def test_raises_character(self):
        with self.assertRaises(TypeError):
            initialize_game(((0, 2), (0, 2)), [{"Name": "Tiny"}, {"stats": 0}])

    def test_board_type(self):
        game = initialize_game(((0, 2), (0, 2)), {"Name": "Tiny", "stats": 0})
        self.assertEqual(type(game[0]), tuple)

    def test_character_type(self):
        game = initialize_game(((0, 5), (0, 5)), {"Name": "Big", "stats": 0})
        self.assertEqual(type(game[1]), dict)

    def test_game_type(self):
        game = initialize_game(((0, 10), (0, 10)), {"Name": "Big", "stats": 12398})
        self.assertEqual(type(game), tuple)
