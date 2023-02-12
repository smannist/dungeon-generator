import pygame
from random import randint
from entities.bsp_tree import BSPTree
from services.dungeon_generator import DungeonGenerator
from services.biome_generator import BiomeGenerator

colors = {
    "#": (160, 110, 90),
    "*": (0, 128, 0),
    ".": (85, 53, 40),
}

class UI:
    """ A Class for user interface
    """
    def __init__(self, block_size=7):
        self.block_size = block_size
        self.height = 0
        self.width = 0
        self.dungeon_generator = None
        self.screen = None
        self.dungeon = None
        self.biome = None

    def run(self):
        """ Method for starting the UI
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 1100))
        self.screen.fill((50, 50, 50))
        self.draw_menu()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.generate_dungeon_button.collidepoint(pos):
                        self.draw_dungeon()
                        self.show_dungeon()
                    elif self.generate_biome_button.collidepoint(pos):
                        self.draw_biome()
                        self.show_biome()
            pygame.display.update()

    def draw_menu(self):
        """ Method for drawing the menu
        """
        font = pygame.font.Font(None, 36)
        self.generate_dungeon_button = pygame.draw.rect(self.screen, (111,85,12), (250, 10, 250, 50))
        self.generate_biome_button = pygame.draw.rect(self.screen, (111,85,12), (250, 70, 250, 50))
        text_dungeon = font.render("Generate Dungeon", True, (255, 255, 255))
        text_biome = font.render("Generate Biome", True, (255, 255, 255))
        self.screen.blit(text_dungeon, (270, 20))
        self.screen.blit(text_biome, (270, 80))

    def show_dungeon(self):
        """ Method for displaying the dungeon on canvas
        """
        bsp_tree = BSPTree(150,100)
        self.dungeon_generator = DungeonGenerator(bsp_tree)
        self.dungeon_generator.generate_dungeon()
        self.height = self.dungeon_generator.height
        self.width = self.dungeon_generator.width
        self.dungeon = self.dungeon_generator.dungeon

    def show_biome(self):
        self.biome_generator = BiomeGenerator(30000,150,100)
        self.biome_generator.generate_biome()
        self.height = self.biome_generator.height
        self.width = self.biome_generator.width
        self.biome = self.biome_generator.biome

    def draw_dungeon(self):
        """ Method for rendering the dungeon
        """
        if self.dungeon is None:
            return
        screen_center_x = self.screen.get_width() // 2
        screen_center_y = self.screen.get_height() // 2
        start_x = screen_center_x - self.width * self.block_size // 2
        start_y = screen_center_y - self.height * self.block_size // 2

        for y in range(self.height):
            for x in range(self.width):
                pos_x = start_x + x * self.block_size
                pos_y = start_y + y * self.block_size
                if self.dungeon[x][y] == "#" or self.dungeon[x][y] == "*":
                    color = colors["#"]
                else:
                    color = colors["."]
                pygame.draw.rect(self.screen, color, (pos_x-20, pos_y, self.block_size, self.block_size))

    def draw_biome(self):
        """ Method for rendering the biome
        """
        if self.biome is None:
            return
        screen_center_x = self.screen.get_width() // 2
        screen_center_y = self.screen.get_height() // 2
        start_x = screen_center_x - self.width * self.block_size // 2
        start_y = screen_center_y - self.height * self.block_size // 2

        for y in range(self.height):
            for x in range(self.width):
                pos_x = start_x + x * self.block_size
                pos_y = start_y + y * self.block_size
                if self.biome[x][y] == "#":
                    color = colors["#"]
                else:
                    color = colors["."]
                pygame.draw.rect(self.screen, color, (pos_x-20, pos_y, self.block_size, self.block_size))
