import unittest
from weapon import Weapon


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon()

    def test_strng_representation(self):
        self.assertEqual(str(self.weapon), "weapon: damage 20")

    def test__gt__when_is_greater(self):
        other = Weapon("weapon", 3)
        self.assertTrue(self.weapon > other)

    def test__gt__when_is_not_greater(self):
        other = Weapon("weapon", 30)
        self.assertFalse(self.weapon > other)

    def test_negative_damage(self):
        with self.assertRaises(ValueError):
            Weapon("a", -1)


if __name__ == '__main__':
    unittest.main()
