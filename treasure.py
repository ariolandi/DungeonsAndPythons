from weapon import Weapon
from spell import Spell
from utils import verify_types, verify_positive, verify_value


"""
Treasure class
--------------
Fields:
type: str - type of treasure (weapon, spell or health/mana potion)
item: object - Weapon, Spell or potion's points
--------------
Methods:
__str__() -> str: string representation
"""


class Treasure:
    @verify_positive
    @verify_types(value_type=str, value=int, name=[str, None])
    def __init__(self, value_type, value, name=None):
        self.type = value_type
        if value_type == 'weapon':
            self.item = Weapon(name=name, damage=value)
        elif value_type == 'spell':
            self.item = Spell(name=name, damage=value)
        else:
            verify_value(self.type, ['health', 'mana'])
            self.type += ' potion'
            self.item = value

    def __str__(self):
        return f"{self.type}, {self.item}"
