import unittest
from hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(
            name="Bron",
            title="Dragonslayer",
            health=100,
            mana=100,
            regeneration_rate=2
        )

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the Dragonslayer")

    def test_dead_hero(self):
        self.hero.take_damage(120)
        self.assertFalse(self.hero.is_alive())

    def test_regenerate(self):
        self.hero.regenerate()
        self.assertEqual(self.hero.health, 102)
        self.assertEqual(self.hero.mana, 102)

    def test_regenerate_dead_hero(self):
        self.hero.take_damage(120)
        with self.assertRaises(Exception):
            self.hero.regenerate()

    def test_string_representation(self):
        expected_string = """Bron the Dragonslayer: \
health 100, mana 100\n"""
        self.assertEqual(str(self.hero), expected_string)

    def test_string_representation_with_weapon(self):
        from weapon import Weapon
        self.hero.equip_weapon(Weapon("Sword", 20))
        expected_string = """Bron the Dragonslayer: \
health 100, mana 100\nweapon: Sword: damage 20\n"""
        self.assertEqual(str(self.hero), expected_string)

    def test_string_representation_with_spell(self):
        from spell import Spell
        self.hero.learn_spell(Spell("Fire", 20, 4, 2))
        expected_string = """Bron the Dragonslayer: \
health 100, mana 100\nspell: Fire: damage 20, mana 4, range 2\n"""
        self.assertEqual(str(self.hero), expected_string)

    def test_string_representation_with_weapon_and_spell(self):
        from weapon import Weapon
        from spell import Spell
        self.hero.equip_weapon(Weapon("Sword", 20))
        self.hero.learn_spell(Spell("Fire", 20, 4, 2))
        expected_string = """Bron the Dragonslayer: \
health 100, mana 100\nweapon: Sword: damage 20\n\
spell: Fire: damage 20, mana 4, range 2\n"""
        self.assertEqual(str(self.hero), expected_string)

    def test_atack_enemy_with_none(self):
        from enemy import Enemy
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        self.assertIsNone(self.hero.attack(enemy, 'weapon'))
        self.assertIsNone(self.hero.attack(enemy, 'spell'))
        self.assertEqual(enemy.health, 100)

    def test_atack_enemy_with_weapon(self):
        from enemy import Enemy
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        from weapon import Weapon
        self.hero.equip_weapon(Weapon("Sword", 20))
        self.hero.attack(enemy, 'weapon')
        self.assertEqual(enemy.health, 80)

    def test_atack_enemy_with_spell(self):
        from enemy import Enemy
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        from spell import Spell
        self.hero.learn_spell(Spell("Fire", 20, 4, 2))
        self.hero.attack(enemy, 'spell')
        self.assertEqual(enemy.health, 80)
        self.assertEqual(self.hero.mana, 96)

    def test_atack_enemy_with_random(self):
        from enemy import Enemy
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        from weapon import Weapon
        from spell import Spell
        self.hero.equip_weapon(Weapon("Sword", 20))
        self.hero.learn_spell(Spell("Fire", 20, 4, 2))
        self.hero.attack(enemy)
        self.assertEqual(enemy.health, 80)
        self.assertEqual(self.hero.mana, 100)

    def test_atack_dead_enemy(self):
        from enemy import Enemy
        enemy = Enemy(health=100, mana=100, damage=20, mana_cost=2)
        enemy.take_damage(120)
        with self.assertRaises(ValueError):
            self.hero.attack(enemy)

    def test_attack_not_enemy(self):
        from character import Character
        character = Character(health=100, mana=100)
        with self.assertRaises(TypeError):
            self.hero.attack(character)


if __name__ == '__main__':
    unittest.main()
