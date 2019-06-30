from character import Character, verify_alive
from utils import verify_positive, verify_types, verify_value
from treasure import Treasure


"""
Hero class
inherits Character
----------
Fields:
name: str - hero's name
title: str - hero's title/nickname
regeneration_rate: int - a small amount of health/mana points
                         that can be regenerated
-----------
Methods:
known_as() -> str - return the full name (name + title) of the hero
__str__() -> str - string representation of the hero (hero's info)
[private]__verify_hero(Enemy) -> None/TypeError/ValueError - verifies 
                            if the given argument can be attacked
take_treasure(Treasure) -> None - loads the treasure according to the type
regenerate() -> None - restore a small amount of health/mana points
attack(Enemy) -> None - attacks the enemy
"""


class Hero(Character):
    @verify_positive
    @verify_types(name=str, title=str, health=int, mana=int, regeneration_rate=int)
    def __init__(self, name, title, health, mana, regeneration_rate):
        Character.__init__(
            self,
            health=health,
            mana=mana,
        )
        self.name = name
        self.title = title
        self.regeneration_rate = regeneration_rate

    def known_as(self):
        return f"{self.name} the {self.title}"

    def __str__(self):
        str_hero = f"{self.known_as()}: health {self.health}, \
mana {self.mana}\n"
        if self.weapon is not None:
            str_hero += "weapon: " + str(self.weapon) + "\n"
        if self.spell is not None:
            str_hero += "spell: " + str(self.spell) + "\n"
        return str_hero

    def __verify_enemy(self, enemy):
        from enemy import Enemy
        if not isinstance(enemy, Enemy):
            raise TypeError("Heroes attack only enemies")
        if enemy.is_alive() is False:
            raise ValueError("The enemy is already dead")

    @verify_types(treasure=Treasure)
    def take_treasure(self, treasure):
        if treasure.type == 'weapon':
            self.equip_weapon(treasure.item)
        elif treasure.type == 'spell':
            self.learn_spell(treasure.item)
        elif treasure.type == 'mana potion':
            self.take_mana(treasure.item)
        elif treasure.type == 'health potion':
            self.take_healing(treasure.item)

    def regenerate(self):
        self.take_mana(self.regeneration_rate)
        self.take_healing(self.regeneration_rate)

    @verify_alive
    @verify_types(by=[str, None])
    def attack(self, enemy, by=None):
        verify_value(by, ['weapon', 'spell', None])
        self.__verify_enemy(enemy)
        if by == 'weapon':
            self.use_weapon(enemy)
        elif by == 'spell':
            self.cast_spell(enemy)
        else:
            if self.weapon is not None:
                self.use_weapon(enemy)
            elif self.spell is not None:
                self.cast_spell(enemy)
