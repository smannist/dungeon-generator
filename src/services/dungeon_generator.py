from entities.bsptree import BSPTree, BSPNode

class DungeonGenerator:
    """ Generates a random dungeon using BSPTree
    Args:
        min_room_size (int): minimum size of a room
        max_room_size (int): maximum size of a room
        map_width (int): width of the map
        map_height (int): height of the map
    """
    def __init__(self, min_room_size, max_room_size, map_width, map_height):
        self.min_room_size = min_room_size
        self.max_room_size = max_room_size
        self.map_width = map_width
        self.map_height = map_height

    def initialize(self):
        """ Initialize an empty row x column map
        Returns:
                map (list): two dimensional map in list form
        """
        map = []
        for x in range(self.map_width):
            row = []
            for y in range(self.map_height):
                row.append(1)
                map.append(row) 
        return map
