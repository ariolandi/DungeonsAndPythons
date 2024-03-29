from character import Character, verify_alive
from utils import verify_positive, verify_types


"""
Enemy class
inherits Character
-----------
Fields:
damage: int -> how much damage the enemy can cause
mana_cost: int -> how much mana costs every attack
-----------
Methods:
__str__() -> str - string representation (enemy info)
[private]__verify_hero(Hero) -> None/TypeError/ValueError - verifies
                            if the given argument can be attacked
attack(Hero) -> None - attacks the hero and causes damages
"""


class Enemy(Character):
    @verify_positive
    @verify_types(health=int, mana=int, damage=int, mana_cost=int)
    def __init__(self, health, mana, damage, mana_cost):
        Character.__init__(
            self,
            health=health,
            mana=mana
        )
        self.damage = damage
        self.mana_cost = mana_cost

    def __str__(self):
        return f"Enemy: health {self.health}, mana {self.mana}\n"

    def __verify_hero(self, hero):
        from hero import Hero
        if not isinstance(hero, Hero):
            raise TypeError("Enemies attack only heroes")
        if hero.is_alive() is False:
            raise ValueError("The hero is already dead")

    @verify_alive
    def attack(self, hero):
        self.__verify_hero(hero)
        if self.mana >= self.mana_cost:
            hero.take_damage(self.damage)
            self.reduce_mana(self.mana_cost)
