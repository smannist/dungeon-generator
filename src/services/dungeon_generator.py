import heapq
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
        self.dungeon = []

    def generate_dungeon(self):
        """ Method for generating the dungeon
        """
        self.initialize_map()
        self.create_rooms()
        self.connect_rooms(self.bsp_tree)

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
        for leaf in self.leaf_nodes:
            room_width = round(randrange(30, 80) / 100 * leaf.width)
            room_height = round(randrange(30, 80) / 100 * leaf.height)

            leaf.room = Room(leaf.x, leaf.y, room_height, room_width)

            for x in range(leaf.room.x, leaf.room.xy):
                for y in range(leaf.room.y, leaf.room.yx):
                    if 0 <= x < len(self.dungeon) and 0 <= y < len(self.dungeon[0]):
                        self.dungeon[x][y] = "#"
                    else:
                        continue

    def draw_pathways(self, path):
        """ Method for drawing the pathways on dungeon map
        """
        if path is not None:
            for i in range(len(path)-1):
                start_node = path[i]
                end_node = path[i + 1]
                x1, y1 = start_node.x, start_node.y
                x2, y2 = end_node.x, end_node.y

                randomize_axis = randrange(0, 2)

                if randomize_axis == 0:
                    x1 = x1 if x1 < x2 else x2
                    x2 = x2 if x1 < x2 else x1
                    for x in range(x1, x2):
                        self.dungeon[x][y1] = "*"
                        self.dungeon[x][y1+1] = "*"
                else:
                    y1 = y1 if y1 < y2 else y2
                    y2 = y2 if y1 < y2 else y1
                    for y in range(y1, y2):
                        self.dungeon[x1][y] = "*"
                        self.dungeon[x1+1][y+1] = "*"

    def connect_rooms(self, bsp_tree):
        """ Method for connecting the rooms using A* search algorithm
        Returns:
            list: pathways
        """
        leaf_nodes = bsp_tree.leaf_nodes
        start = leaf_nodes[0]
        paths = []

        for start in leaf_nodes:
            visited = set()
            heap = [(0, start, [start])]
            while heap:
                (cost, node, path) = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                paths.append(path)
                self.draw_pathways(path)
                for (neighbor_cost, neighbor) in self.get_neighbors(node, leaf_nodes):
                    heapq.heappush(heap, (cost + neighbor_cost, neighbor, path + [neighbor]))

        return paths

    def get_neighbors(self, node, leaf_nodes):
        """ Method for finding neighbouring nodes
        Returns:
            list: neighbouring nodes
        """
        x1, y1 = node.x, node.y
        threshold = 28
        neighbors = []

        for leaf in leaf_nodes:
            x2, y2 = leaf.x, leaf.y
            distance = abs(x2 - x1) + abs(y2 - y1) - 13
            if distance <= threshold:
                cost = abs(leaf.x - leaf_nodes[-1].x) + abs(leaf.y - leaf_nodes[-1].y) - 150
                neighbors.append((cost, leaf))

        return neighbors
