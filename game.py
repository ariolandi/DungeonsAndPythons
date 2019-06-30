from dungeon import Dungeon
from hero import Hero
from enemy import Enemy


"""
Game class
----------
Fields:
hero: Hero - player's character
levels: int - amound of levels in the game
dungeon: Dungeon - a current level's dungeon
finished: bool - a game end indicator
----------
Methods:
[private]__narrator() -> None - prints the instructions for the game;
                       creates player's character
[private]__enter_direction() -> str - takes user input and formats it
[private]__enter_attack_weapon() -> str - takes user input and formats it
[private]__fight() -> None - simulates a battle with an enemy
[private]__play() -> None - simulates one level of the game
[private]__next_level(int) -> None - loads next dungeon
start() -> None - simulates a game
"""


class Game:
    def __init__(self, levels):
        self.hero = None
        self.levels = levels
        self.dungeon = None
        self.finished = False

    def __narrator(self):
        welcome = f"""----Hello, my little friend----\n\
Welcome to our world of adventures. You will have to pass {self.levels} \
to end this game. Follow my instructions:\n"""
        print(welcome)
        name = input("Enter your character's name: >>")
        title = input("Enter your character's title: >>")
        self.hero = Hero(
            name=name,
            title=title,
            health=100,
            mana=100,
            regeneration_rate=5)
        directions = f"""Hello, {self.hero.known_as()}, nice to meet you!\n
Soon you will see the first map you have to pass. To move through it you can use:\n\
d - down\nu - up\nr - right\nl - left\n"""
        symbols = """Also, there is some special symbols in your way:\n\
# - walls\n. - free space\n\
H - you are here\nE - there is an enemy here\nT - there is a treasure here\nG - this is a gate \
to the next level\n"""
        battle_instructions = """In your journey through this land you will meen some enemies. \
In the battles with them you will have to choose your action:\n\
r - regenerate health and mana\nw - attack with a weapon\ns - attack with a spell\n- - don't attack at all\n
Wish you luck!"""
        print(directions)
        print(symbols)
        print(battle_instructions)

    def __enter_direction(self):
        direction = input(">>")
        direction_list = {
            "d": "down",
            "u": "up",
            "l": "left",
            "r": "right"
        }
        return direction_list[direction]

    def __enter_attack_weapon(self):
        weapon = input("attack by (r/w/s/-) >>")
        while weapon == "r":
            self.hero.regenerate()
            print("health:", self.hero.health, "mana:", self.hero.mana)
            weapon = input("attack by (r/w/s/-) >>")
        weapon_list = {
            "w": "weapon",
            "s": "spell",
            "-": None
        }
        return weapon_type[weapon]

    def __fight(self):
        print("----in fight----")
        print (str(self.hero), "vs\n", str(self.dungeon.enemy))

        while self.hero.is_alive() and self.dungeon.enemy.is_alive():
            try:
                self.hero.attack(self.dungeon.enemy, self.__enter_attack_weapon())
                self.dungeon.enemy.attack(self.hero)
            except Exception:
                pass

            print(str(self.hero), str(self.dungeon.enemy))

        if self.hero.is_alive():
            print("You win!")
        else:
            print("You are dead!")
            self.dungeon.finished = True
            self.game.finished = True

        self.dungeon.enemy = None
        self.dungeon.battle = False

    def __play(self):
        while self.dungeon.finished is False:
            self.dungeon.print_map()
            try:
                self.dungeon.move(self.__enter_direction())
            except Exception:
                print("You can't move in this direction!")

            if self.dungeon.battle is True:
                self.__fight()

    def __next_level(self, level):
        self.dungeon = Dungeon(level=level, hero=self.hero)
        self.dungeon.load()
        self.__play()

    def start(self):
        self.__narrator()

        for level in range(1, self.levels + 1):
            self.__next_level(level)
            if self.finished:
                print("You lost! Try again!")
                return None

        self.finished = True
        print("Congratulations! You beat the game!")
