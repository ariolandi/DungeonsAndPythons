import unittest
from treasure import Treasure


class TestTreasure(unittest.TestCase):
    def test_treasure_type_weapon(self):
        from weapon import Weapon
        treasure = Treasure("weapon", 20)
        self.assertEqual(type(treasure.item), Weapon)

    def test_treasure_type_spell(self):
        from spell import Spell
        treasure = Treasure("spell", 20)
        self.assertEqual(type(treasure.item), Spell)

    def test_treasure_type_potion(self):
        treasure = Treasure("health", 20)
        self.assertEqual(str(treasure), "health potion, 20")

    def test_treasure_potion_type_not_expected(self):
        with self.assertRaises(ValueError):
            Treasure("fjghd", 4)


if __name__ == '__main__':
    unittest.main()
