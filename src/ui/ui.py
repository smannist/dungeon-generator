import pygame
from random import randint
from entities.bsp_tree import BSPTree
from services.dungeon_generator import DungeonGenerator

colors = {
    "#": (185, 90, 49),
    "*": (200, 100, 50),
    ".": (84, 38, 18),
    ",": (90, 35, 20),
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

    def run(self):
        """ Method for starting the UI
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 900))
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
                        self.show_dungeon()

            self.draw_dungeon()
            pygame.display.update()

    def draw_menu(self):
        """ Method for drawing the menu
        """
        font = pygame.font.Font(None, 36)
        self.generate_dungeon_button = pygame.draw.rect(self.screen, (111,85,12), (1100, 50, 250, 50))
        text = font.render("Generate Dungeon", True, (255, 255, 255))
        self.screen.blit(text, (1110, 60))

    def show_dungeon(self):
        """ Method for displaying the dungeon on canvas
        """
        bsp_tree = BSPTree(120,80)
        self.dungeon_generator = DungeonGenerator(bsp_tree)
        self.dungeon_generator.generate_dungeon()
        self.height = self.dungeon_generator.height
        self.width = self.dungeon_generator.width
        self.dungeon = self.dungeon_generator.dungeon

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
