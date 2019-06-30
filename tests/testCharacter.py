import unittest
from character import Character


class TestCharacterClass(unittest.TestCase):
    def setUp(self):
        self.dead_character = Character(0, 5)
        self.alive_character = Character(6, 5)

    def test_is_alive_dead_character(self):
        self.assertFalse(self.dead_character.is_alive())

    def test_is_alive_alive_character(self):
        self.assertTrue(self.alive_character.is_alive())

    def test_take_healing_dead_character(self):
        with self.assertRaises(Exception):
            self.dead_character.take_healing(healing_points=7)

    def test_take_healing_alive_character(self):
        self.assertIsNone(self.alive_character.take_healing(healing_points=7))

    def test_take_mana_dead_character(self):
        with self.assertRaises(Exception):
            self.dead_character.take_mana(mana_points=7)

    def test_take_mana_alive_character(self):
        self.assertIsNone(self.alive_character.take_mana(mana_points=7))

    def test_take_damage_to_death(self):
        self.alive_character.take_damage(120)
        self.assertEqual(self.alive_character.health, 0)

    def test_wrong_type_of_points(self):
        with self.assertRaises(TypeError):
            self.alive_character.take_healing(healing_points='a')
            self.alive_character.take_mana(mana_points='a')

    def test_wrong_value_of_points(self):
        with self.assertRaises(ValueError):
            self.alive_character.take_healing(healing_points=-1)
            self.alive_character.take_mana(mana_points=-1)

    def test_equip_weapon(self):
        from weapon import Weapon
        self.assertIsNone(self.alive_character.equip_weapon(Weapon()))

    def test_equip_weapon_with_wrong_type(self):
        with self.assertRaises(TypeError):
            self.alive_character.equip_weapon(5)

    def test_equip_weapon_dead_character(self):
        from weapon import Weapon
        with self.assertRaises(Exception):
            self.dead_character.equip_weapon(Weapon())

    def test_learn_spell(self):
        from spell import Spell
        self.assertIsNone(self.alive_character.learn_spell(Spell()))

    def test_learn_spell_with_wrong_type(self):
        with self.assertRaises(TypeError):
            self.alive_character.learn_spell(5)

    def test_learn_spell_dead_character(self):
        from spell import Spell
        with self.assertRaises(Exception):
            self.dead_character.spell(Spell())


if __name__ == '__main__':
    unittest.main()
