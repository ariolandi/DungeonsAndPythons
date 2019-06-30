from utils import verify_types, verify_direction, take_random
from hero import Hero
from enemy import Enemy
from treasure import Treasure


"""
Dungeon class
-------------
Fields:
level: int - indicates the current level
hero: Hero - player's character
enemy: Enemy - indicates current enemy if has one
map: list[list[string]] - contains dungeon's map
[private]__enemies: list[Enemies] - a list of dungeon's enemies
[private]__treasures: list[Treasures] - a list of dungeon's treasures
[private]__hero_spawn_position: (int, int) - indicates hero's starting position
finished: bool - indicates dungeon's end
battle: bool - indicates a battle
------------
Methods:
[private]__read_file(string) -> list[string] - opens a file and
                                                  returns its content
[private]__fill_treasures_list() -> None - reads the treasures list from a file
[private]__fill_enemies_list() -> None - reads the enemies list from a file
[private]__fill_map() -> None - reads the map from a file
[private]__find_hero_spawn_position() -> None - finds where on the map hero has
                                                to be spawn
[private]__nove_hero_to(row, column) -> None - moves the hero
[private]__collect_treasure() -> None - chooses a treasure from the list and
                                        gives it to the hero
[private]__spawn_enemy() -> None - chooses an enemy from the list and initiates
                                   a battle
[private]__can_move(int, int) -> bool - check if a given position is valid
[private]__inspect(int. int) -> None - checks if there is a special symbol
                                        on this position and make a relevant
                                        action
spawn_hero() -> None - spawns the hero in the starting position
load() -> None - loads treasures and enemies lists, map and spawns the hero
print_map() -> None - displays the map
move(direction) -> None/Exception - tries to move tha hero in a given direction
"""


class Dungeon:
    @verify_types(level=int, hero=[Hero, None])
    def __init__(self, level, hero):
        self.level = level
        self.hero = hero
        self.enemy = None
        self.map = []
        self.__enemies = []
        self.__treasures = []
        self.__hero_spawn_position = (0, 0)
        self.finished = False
        self.battle = False

    def __read_file(self, file_name):
        with open(file_name) as file:
            return file.readlines()

    def __fill_treasures_list(self):
        file_lines = self.__read_file(f"treasures_level{self.level}.txt")
        for line in file_lines:
            treasure_info = line.split()
            treasure_info[1] = int(treasure_info[1])
            self.__treasures.append(Treasure(*treasure_info))

    def __fill_enemies_list(self):
        file_lines = self.__read_file(f"enemies_level{self.level}.txt")
        for line in file_lines:
            enemy_info = [int(info_part) for info_part in line.split(',')]
            self.__enemies.append(Enemy(*enemy_info))

    def __fill_map(self):
        map_info = self.__read_file(f"level{self.level}.txt")
        self.__fill_treasures_list()
        self.__fill_enemies_list()
        self.map = [list(row.replace('\n', '')) for row in map_info]

    def __find_hero_spawn_position(self):
        for row in range(0, len(self.map)):
            for column in range(0, len(self.map[row])):
                if self.map[row][column] is 'S':
                    self.__hero_spawn_position = (row, column)
                    return None

    def __move_hero_to(self, row, column):
        old_row, old_column = self.hero.position
        self.map[old_row][old_column] = '.'
        self.hero.position = (row, column)
        self.map[row][column] = 'H'

    def __collect_treasure(self):
        treasure = take_random(self.__treasures)
        print("You found a treasure!", str(treasure))
        self.hero.take_treasure(treasure)

    def __spawn_enemy(self):
        self.enemy = take_random(self.__enemies)
        print("You found an enemy! A battle is about to start!")
        self.battle = True

    def __can_move(self, row, column):
        if self.map[row][column] is not '#' and\
           row >= 0 and row < len(self.map) and\
           column >= 0 and column < len(self.map[row]):
            return True
        return False

    def __inspect(self, row, column):
        symbol = self.map[row][column]
        if symbol is 'G':
            print("You found a gate! You go to the next level!")
            self.finished = True
        elif symbol is 'T':
            self.__collect_treasure()
        elif symbol is 'E':
            self.__spawn_enemy()

    def spawn_hero(self):
        self.hero.position = self.__hero_spawn_position
        row, column = self.hero.position
        self.map[row][column] = 'H'

    def load(self):
        self.__fill_map()
        self.__fill_enemies_list()
        self.__fill_treasures_list()
        self.__find_hero_spawn_position()
        self.spawn_hero()

    def print_map(self):
        for row in self.map:
            print(' '.join(row))

    @verify_direction
    def move(self, direction):
        row, column = self.hero.position
        move_to = {
            "up": (row - 1, column),
            "down": (row + 1, column),
            "right": (row, column + 1),
            "left": (row, column - 1)
        }
        row, column = move_to[direction]
        if self.__can_move(row, column):
            self.__inspect(row, column)
            self.__move_hero_to(row, column)
        else:
            raise Exception("Wrong direction")
