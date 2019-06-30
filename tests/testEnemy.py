import unittest
from enemy import Enemy


class TestHero(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(
            health=100,
            mana=100,
            damage=20,
            mana_cost=2
        )

    def test_attack_hero(self):
        from hero import Hero
        hero = Hero(
            name="hero",
            title="brave",
            health=100,
            mana=100,
            regeneration_rate=2
        )
        self.enemy.attack(hero)
        self.assertEqual(hero.health, 80)
        self.assertEqual(self.enemy.mana, 98)

    def test_attack_not_hero(self):
        from character import Character
        character = Character(health=100, mana=100)
        with self.assertRaises(TypeError):
            self.enemy.attack(character)

    def test_attack_dead_hero(self):
        from hero import Hero
        hero = Hero(
            name="hero",
            title="brave",
            health=10,
            mana=100,
            regeneration_rate=2
        )
        hero.take_damage(10)
        with self.assertRaises(ValueError):
            self.enemy.attack(hero)

    def test_attack_when_dead(self):
        from hero import Hero
        hero = Hero(
            name="hero",
            title="brave",
            health=100,
            mana=100,
            regeneration_rate=2
        )
        self.enemy.take_damage(120)
        with self.assertRaises(Exception):
            self.enemy.attack(hero)

    def test_attack_with_not_enough_mana(self):
        from hero import Hero
        hero = Hero(
            name="hero",
            title="brave",
            health=100,
            mana=100,
            regeneration_rate=2
        )
        self.enemy.reduce_mana(100)
        self.assertIsNone(self.enemy.attack(hero))

    def test_string_representation(self):
        expected_string = "Enemy: health 100, mana 100\n"
        self.assertEqual(str(self.enemy), expected_string)



if __name__ == '__main__':
    unittest.main()
