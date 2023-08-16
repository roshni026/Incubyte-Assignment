import unittest
from src.spaceship import Spaceship

class TestSpaceship(unittest.TestCase):
    def test_move_forward(self):
        spacecraft = Spaceship()
        spacecraft.execute_command("f")
        self.assertEqual(spacecraft.get_position(), (0, 1, 0))

    def test_move_backward(self):
        spacecraft = Spaceship()
        spacecraft.execute_command("b")
        self.assertEqual(spacecraft.get_position(), (0, -1, 0))

    def test_turn_left(self):
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("l")
        self.assertEqual(spacecraft.get_direction(), "W")

    def test_turn_right(self):
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("r")
        self.assertEqual(spacecraft.get_direction(), "E")

    def test_turn_up(self):
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("u")
        self.assertEqual(spacecraft.get_direction(), "Up")

    def test_turn_down(self):
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("d")
        self.assertEqual(spacecraft.get_direction(), "Down")

    def test_e2e_scenario(self):
        spacecraft = Spaceship()
        commands = ["f", "r", "u", "b", "l"]
        for command in commands:
            spacecraft.execute_command(command)
        self.assertEqual(spacecraft.get_position(), (0, 1, -1))
        self.assertEqual(spacecraft.get_direction(), "Up")

    def test_invalid_command(self):
        spacecraft = Spaceship()
        with self.assertRaises(ValueError):
            spacecraft.execute_command("x")

if __name__ == '__main__':
    unittest.main()