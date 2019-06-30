from utils import verify_positive, verify_types


"""
Wapon class
-----------
Fields:
name: str - weapons name
damage: int - how mush damage the weapon causes when used
-----------
Methods:
__str__() -> str - string representation of the weapon
__gt__(Weapon) -> bool - operator > (in damage)
"""


class Weapon:
    @verify_positive
    @verify_types(str, int)
    def __init__(self, name='weapon', damage=20):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name}: damage {self.damage}"

    def __gt__(self, other):
        return self.damage > other.damage
