from unittest import TestCase
from Modules.character import check_alive


class Test(TestCase):

    def test_dead(self):
        my_guy = {"Motivation": 0, "alive": True}
        self.assertEqual(check_alive(my_guy), False)

    def test_alive(self):
        my_guy = {"Motivation": 20, "alive": True}
        self.assertEqual(True, check_alive(my_guy))

    def test_raises_type(self):
        with self.assertRaises(TypeError):
            check_alive([])

    def test_raises_value_motivation(self):
        with self.assertRaises(ValueError):
            check_alive({"alive": True})

    def test_raises_value_alive(self):
        with self.assertRaises(ValueError):
            check_alive({"Motivation": 0})

    def test_raises_type_val_motivation(self):
        with self.assertRaises(TypeError):
            check_alive({"Motivation": '0', "alive": True})
