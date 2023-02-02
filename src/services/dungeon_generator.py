from random import randrange
from entities.room import Room

class DungeonGenerator:
    """ A class which generates the dungeon
    Args:
        bsp_tree (BSPTree): Contains info for mapping
    """
    def __init__(self, bsp_tree):
        self.bsp_tree = bsp_tree
        self.root = bsp_tree.root
        self.height = bsp_tree.height
        self.width = bsp_tree.width
        self.leaf_nodes = bsp_tree.leaf_nodes
        self.rooms = []
        self.dungeon = []

    def generate_dungeon(self):
        """ Method for generating the dungeon
        """
        self.bsp_tree.split_node(self.root)
        self.initialize_map()
        self.create_rooms()

    def initialize_map(self):
        """ Method for initializing the map. Initially dungeon map is just dots means wall.
        """
        self.dungeon = []
        for _ in range(self.width):
            row = []
            for _ in range(self.height):
                row.append(".")
            self.dungeon.append(row)

    def create_rooms(self):
        """ Method for creating the rooms. Rooms are marked with # on the dungeon matrix map.
        """

        skip_rooms = randrange(0,3)
        self.leaf_nodes = self.leaf_nodes[skip_rooms:]

        for leaf in self.leaf_nodes:
            room_width = round(randrange(40, 70) / 100 * leaf.width)
            room_height = round(randrange(40, 70) / 100 * leaf.height)

            leaf.room = Room(leaf.x, leaf.y, room_height, room_width)

            for x in range(leaf.room.x, leaf.room.xy):
                for y in range(leaf.room.y, leaf.room.yx):
                    self.dungeon[x][y] = "#"
