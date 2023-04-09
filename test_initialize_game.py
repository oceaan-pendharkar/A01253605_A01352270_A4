from unittest import TestCase
from board import initialize_game


class Test(TestCase):
    def test_small_board(self):
        self.assertEqual((((0, 2), (0, 2)), {"Name": "Tiny", "stats": 0}), initialize_game(((0, 2), (0, 2)),
                                                                                        {"Name": "Tiny", "stats": 0}))
