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
        self.hero.learn_spell(Spell("Fire", 20, 4, 2))
        self.hero.equip_weapon(Weapon("Sword", 20))
        expected_string = """Bron the Dragonslayer: \
health 100, mana 100\nweapon: Sword: damage 20\n\
spell: Fire: damage 20, mana 4, range 2\n"""
        self.assertEqual(str(self.hero), expected_string)


if __name__ == '__main__':
    unittest.main()
