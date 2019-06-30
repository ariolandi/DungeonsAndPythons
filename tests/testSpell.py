import unittest
from spell import Spell


class TestSpell(unittest.TestCase):
    def setUp(self):
        self.spell = Spell()

    def test_strng_representation(self):
        self.assertEqual(str(self.spell), "spell: damage 20, mana 20, range 2")

    def test__gt__when_is_greater(self):
        other = Spell("Spell", 3, 1, 1)
        self.assertTrue(self.spell > other)

    def test__gt__when_is_not_greater(self):
        other = Spell("Spell", 30, 50, 10)
        self.assertFalse(self.spell > other)

    def test_one_negative_value(self):
        with self.assertRaises(ValueError):
            Spell("a", 0, -1, 3)


if __name__ == '__main__':
    unittest.main()
