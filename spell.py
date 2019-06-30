from utils import verify_positive, verify_types


"""
Spell class
-----------
Fields:
name: str - spell name name
damage: int - how mush damage the spell causes when used
mana_cost: int - how mush mana the cpell costs to be cast
cast_range: int - in what range can cause damage
-----------
Methods:
__str__() -> str - string representation of the string
__gt__(Spell) -> bool - operator >
"""


class Spell:
    @verify_positive
    @verify_types(name=str, damage=int, mana_cost=int, cast_range=int)
    def __init__(self, name="spell", damage=20, mana_cost=20, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return f"{self.name}: damage {self.damage}, \
mana {self.mana_cost}, range {self.cast_range}"

    def __gt__(self, other):
        return (self.damage * self.cast_range) - self.mana_cost >\
            (other.damage * other.cast_range) - other.mana_cost
