from random import randrange
from entities.room import Room

class DungeonGenerator:
    """ A class which generates the dungeon
    Args:
        bsp_tree (BSPTree): Contains info for mapping
    """
    def __init__(self, bsp_tree, min_room_size, max_room_size):
        self.bsp_tree = bsp_tree
        self.root = bsp_tree.root
        self.height = bsp_tree.height
        self.width = bsp_tree.width
        self.leaf_nodes = bsp_tree.leaf_nodes
        self.max_room_size = max_room_size
        self.min_room_size = min_room_size
        self.dungeon = []

    def generate_dungeon(self):
        """ Method for generating the dungeon
        """
        self.initialize_map()
        self.create_rooms()
        self.connect_rooms()

    def initialize_map(self):
        """ Method for initializing the map.
            Initially dungeon map is just dots (or the symbol ".") which represents a wall.
        """
        self.dungeon = []
        for _ in range(self.width):
            row = []
            for _ in range(self.height):
                row.append(".")
            self.dungeon.append(row)

    def create_rooms(self):
        """ Method for creating the rooms.
            Rooms are marked with # on the dungeon matrix map.
        """

        # skip a few rooms to make the dungeon look less crowded (also increases randomization)
        for _ in range(0, 9):
            skip_room = randrange(0, len(self.leaf_nodes))
            self.leaf_nodes.pop(skip_room)

        for leaf in self.leaf_nodes:
            room_width = round(randrange(self.min_room_size, self.max_room_size) \
                                                             / 100 * leaf.width)
            room_height = round(randrange(self.min_room_size, self.max_room_size) \
                                                             / 100 * leaf.height)

            leaf.room = Room(leaf.x, leaf.y, room_height, room_width)

            for x in range(leaf.room.x, leaf.room.xy):
                for y in range(leaf.room.y, leaf.room.yx):
                    if 0 <= x < len(self.dungeon) and 0 <= y < len(self.dungeon[0]):
                        self.dungeon[x][y] = "#"
                    else:
                        continue

    def connect_rooms(self):
        """ Method for connecting the rooms with paths.
            Paths are marked with * on the dungeon matrix map.
        """
        room_centers = self.get_room_centers()

        for i in range(len(room_centers)-1):
            start = room_centers[i]
            end = room_centers[i + 1]
            x1, y1 = start
            x2, y2 = end

            if x1 is not x2:

                if x2 > x1:
                    x_increment = 1
                else:
                    x_increment = -1

                for x in range(x1, x2, x_increment):
                    self.dungeon[x][y1] = "*"

            if y1 is not y2:

                if y2 > y1:
                    y_increment = 1
                else:
                    y_increment = -1

                for y in range(y1, y2, y_increment):
                    self.dungeon[x2][y] = "*"

    def get_room_centers(self):
        """ Method for iterating through list of BSP Tree leaves
            and getting coordinates of rooms centers.
        Returns:
            list: center of the rooms
        """
        room_centers = []

        for leaf in self.leaf_nodes:
            room_centers.append(leaf.room.center)

        return room_centers
