import unittest
from character import Character
from weapon import Weapon
from spell import Spell
from enemy import Enemy





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

    def test_reduce_mana_alive_character(self):
        self.alive_character.reduce_mana(3)
        self.assertEqual(self.alive_character.mana, 2)

    def test_reduce_mana_to_0_alive_character(self):
        self.alive_character.reduce_mana(10)
        self.assertEqual(self.alive_character.mana, 0)

    def test_reduce_mana_dead_character(self):
        with self.assertRaises(Exception):
            self.dead_character.reduce_mana(2)

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
        self.assertIsNone(self.alive_character.equip_weapon(Weapon()))

    def test_equip_weapon_with_wrong_type(self):
        with self.assertRaises(TypeError):
            self.alive_character.equip_weapon(5)

    def test_equip_weapon_dead_character(self):
        with self.assertRaises(Exception):
            self.dead_character.equip_weapon(Weapon())

    def test_learn_spell(self):
        self.assertIsNone(self.alive_character.learn_spell(Spell()))

    def test_learn_spell_with_wrong_type(self):
        with self.assertRaises(TypeError):
            self.alive_character.learn_spell(5)

    def test_learn_spell_dead_character(self):
        with self.assertRaises(Exception):
            self.dead_character.spell(Spell())

    def test_weapon_usage_with_none(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        self.assertIsNone(self.alive_character.use_weapon(enemy))
        self.assertEqual(enemy.health, 100)

    def test_weapon_usage_with_sword(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        self.alive_character.equip_weapon(Weapon("Sword", 20))
        self.assertIsNone(self.alive_character.use_weapon(enemy))
        self.assertEqual(enemy.health, 80)

    def test_weapon_usage_with_dead_character(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        with self.assertRaises(Exception):
            self.dead_character.use_weapon(enemy)

    def test_cast_spell_with_none(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        self.alive_character.cast_spell(enemy)
        self.assertEqual(enemy.health, 100)
        self.assertEqual(self.alive_character.mana, 5)

    def test_cast_spell_with_enough_mana(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        self.alive_character.learn_spell(Spell("Fire", 20, 4, 2))
        self.alive_character.cast_spell(enemy)
        self.assertEqual(enemy.health, 80)
        self.assertEqual(self.alive_character.mana, 1)

    def test_cast_spell_with_not_enough_mana(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        self.alive_character.reduce_mana(10)
        self.alive_character.learn_spell(Spell("Fire", 20, 4, 2))
        self.alive_character.cast_spell(enemy)
        self.assertEqual(enemy.health, 100)

    def test_cast_spell_with_dead_character(self):
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        with self.assertRaises(Exception):
            self.dead_character.cast_spell(enemy)


if __name__ == '__main__':
    unittest.main()
