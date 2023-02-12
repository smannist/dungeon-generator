from services.random_walk import RandomWalk

class BiomeGenerator:
    """ A class which generates the biome
    Args:
        width (int): map width
        height (int): map height
        steps (int): number of steps
    """
    def __init__(self,steps,width,height):
        self.width = width
        self.height = height
        self.steps = steps
        self.biome = []

        self.random_walk = RandomWalk(steps, self.width, self.height)
        self.random_walk.walk_randomly()
        self.walk_coordinates = self.random_walk.get_walk_coordinates()

    def generate_biome(self):
        """ Method for generating the biome
        """
        self.initialize_map()
        self.draw_biome()

    def initialize_map(self):
        """ Method for initializing the map.
            Initially dungeon map is just dots which represents a wall.
        """
        self.biome = []
        for _ in range(self.width):
            row = []
            for _ in range(self.height):
                row.append(".")
            self.biome.append(row)

    def draw_biome(self):
        """ Method which draws the biome on 2D matrix.
            "#" represents biome area on the map.
        """
        for coordinate in self.walk_coordinates:
            x,y = coordinate
            self.biome[x][y] = "#"
