from utils import verify_types, verify_positive
from weapon import Weapon
from spell import Spell


# verifyig alive character method decorator; used only in Character class
def verify_alive(func):
    def check_alive(self, *args, **kwargs):
        if self.is_alive() is False:
            raise Exception("The character is dead")
        return func(self, *args, **kwargs)
    return check_alive


"""
Character class
---------------
Realises basic character object
---------------
Fields:
health: int - health points; when health reach 0, the character dies
mana: int - mana points; used for spell cast
weapon: Weapon/None - the character's weapon, used in battle
spell: Spell/None - the spell that character may cast
---------------
Methods:
is_alive() -> bool - returns True if character's health is a positive
take_healing(int) -> None - restore some character's health points
take_mana(int) -> None - restore some character's mana points;
take_damade(int) -> None - reduce some character's health points
reduce_mana(int) -> None - reduce some chaacter's mana points
equip_weapon(Weapon) -> None - equip new weapon if the character has none
                               or the new is better than the old one
learn_spell(Spell) -> None - learn new spell if the character has none
                             or the new is better than the old one
use_weapon(Enemy) -> None - attacks the enemy with a weapon if possible
cast_spell(Enemy) -> None - attacks the enemy with a weapon if possible
"""


class Character:
    @verify_positive
    @verify_types(int, int, Weapon, Spell)
    def __init__(self, health=100, mana=100, weapon=None, spell=None):
        self.health = health
        self.mana = mana
        self.weapon = weapon
        self.spell = spell
        self.position = (0, 0)

    def is_alive(self):
        return self.health > 0

    @verify_positive
    @verify_types(int)
    @verify_alive
    def take_healing(self, healing_points):
        self.health += healing_points

    @verify_positive
    @verify_types(int)
    @verify_alive
    def take_mana(self, mana_points):
        self.mana += mana_points

    @verify_positive
    @verify_types([int, float])
    @verify_alive
    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)

    @verify_positive
    @verify_types(mana_points=int)
    @verify_alive
    def reduce_mana(self, mana_points):
        self.mana = max(0, self.mana - mana_points)

    @verify_types(Weapon)
    @verify_alive
    def equip_weapon(self, weapon):
        if self.weapon is None or weapon > self.weapon:
            self.weapon = weapon

    @verify_types(Spell)
    @verify_alive
    def learn_spell(self, spell):
        if self.spell is None or spell > self.self:
            self.spell = spell

    @verify_alive
    def use_weapon(self, enemy):
        if self.weapon is not None:
            enemy.take_damage(self.weapon.damage)

    @verify_alive
    def cast_spell(self, enemy):
        if self.spell is not None and\
           self.mana >= self.spell.mana_cost:
            self.reduce_mana(self.spell.mana_cost)
            enemy.take_damage(self.spell.damage)
