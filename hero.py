from character import Character
from utils import verify_positive, verify_types
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
take_treasure(Treasure) -> None - loads the treasure according to the type
regenerate() -> None - restore a small amount of health/mana points
__str__() -> str - string representation of the hero (hero's info)
"""


class Hero(Character):
    @verify_positive
    @verify_types(name=str, title=str, health=int, mana=int)
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

    @verify_types(treasure=Treasure)
    def take_treasure(self, treasure):
        if treasure.type is 'weapon':
            self.equip_weapon(treasure.item)
        elif treasure.type is 'spell':
            self.learn_spell(treasure.item)
        elif treasure.type is 'mana potion':
            self.take_mana(treasure.item)
        elif treasure.type is 'health potion':
            self.take_healing(treasure.item)

    def regenerate(self):
        self.take_mana(self.regeneration_rate)
        self.take_healing(self.regeneration_rate)

    def __str__(self):
        str_hero = f"{self.known_as()}: health {self.health}, \
mana {self.mana}\n"
        if self.weapon is not None:
            str_hero += "weapon: " + str(self.weapon) + "\n"
        if self.spell is not None:
            str_hero += "spell: " + str(self.spell) + "\n"
        return str_hero
