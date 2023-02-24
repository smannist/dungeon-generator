import pygame
from random import randint
from entities.bsp_tree import BSPTree
from services.dungeon_generator import DungeonGenerator
from services.biome_generator import BiomeGenerator
from ui.slider import Slider

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
        self.screen = None
        self.dungeon_generator = None
        self.dungeon = None
        self.biome = None

        self.max_room_size_slider = Slider(600, 50, 250, 20, 90, 21, (50,50,50), "Max room size: ")
        self.min_room_size_slider = Slider(600, 140, 250, 20, 90, 20, (50,50,50), "Min room size: ")
        self.max_room_size = self.max_room_size_slider.current_value
        self.min_room_size = self.min_room_size_slider.current_value

        self.step_count_slider = Slider(900, 50, 250, 1000, 32000, 1000, (50,50,50), "Random walk steps: ")
        self.random_walk_steps = self.step_count_slider.current_value

        pygame.init()

        self.slider_font = pygame.font.Font(None, 20)
        self.button_font = pygame.font.Font(None, 36)

    def run(self):
        """ Method for starting the UI
        """
        self.screen = pygame.display.set_mode((1600, 1100))
        self.screen.fill((50, 50, 50))

        self.draw_menu()
        self.max_room_size_slider.draw_all(self.screen, self.slider_font)
        self.min_room_size_slider.draw_all(self.screen, self.slider_font)
        self.step_count_slider.draw_all(self.screen, self.slider_font)

        self.menu_loop()

    def menu_loop(self):
        """Method responsible for providing the menu loop
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_position = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()

                    if self.max_room_size_slider.collidepoint(mouse_position):
                        self.max_room_size_slider.update_current_value(mouse_position, mouse_pressed)
                        self.max_room_size_slider.draw_all(self.screen, self.slider_font)
                        self.max_room_size = self.max_room_size_slider.current_value

                        if self.max_room_size <= self.min_room_size:
                            self.increase_maximum_room_size_slider()

                    if self.min_room_size_slider.collidepoint(mouse_position):
                        self.min_room_size_slider.update_current_value(mouse_position, mouse_pressed)
                        self.min_room_size_slider.draw_all(self.screen, self.slider_font)
                        self.min_room_size = self.min_room_size_slider.current_value

                        if self.min_room_size >= self.max_room_size:
                            self.increase_maximum_room_size_slider()

                    if self.step_count_slider.collidepoint(mouse_position):
                        self.step_count_slider.update_current_value(mouse_position, mouse_pressed)
                        self.step_count_slider.draw_all(self.screen, self.slider_font)
                        self.random_walk_steps = self.step_count_slider.current_value

                    if self.generate_dungeon_button.collidepoint(mouse_position):
                        self.setup_dungeon()
                        self.render_dungeon()

                    if self.generate_biome_button.collidepoint(mouse_position):
                        self.setup_biome()
                        self.render_biome()
            pygame.display.update()

    def draw_menu(self):
        """ Method for drawing the menu
        """
        self.generate_dungeon_button = pygame.draw.rect(self.screen, colors["."], (250, 10, 250, 50))
        self.generate_biome_button = pygame.draw.rect(self.screen, colors["."], (250, 70, 250, 50))
        text_dungeon = self.button_font.render("Generate Dungeon", True, (255, 255, 255))
        text_biome = self.button_font.render("Generate Biome", True, (255, 255, 255))
        self.screen.blit(text_dungeon, (270, 20))
        self.screen.blit(text_biome, (270, 80))

    def setup_dungeon(self):
        """ Method for setting up dungeon
        """
        bsp_tree = BSPTree(150,100)
        self.dungeon_generator = DungeonGenerator(bsp_tree, self.min_room_size, self.max_room_size)
        self.dungeon_generator.generate_dungeon()
        self.dungeon = self.dungeon_generator.dungeon
        self.height = self.dungeon_generator.height
        self.width = self.dungeon_generator.width

    def setup_biome(self):
        """ Method for setting up biome
        """
        self.biome_generator = BiomeGenerator(self.random_walk_steps,150,100)
        self.biome_generator.generate_biome()
        self.height = self.biome_generator.height
        self.width = self.biome_generator.width
        self.biome = self.biome_generator.biome

    def render_dungeon(self):
        """ Method for rendering the dungeon
        """
        if self.dungeon is None:
            return
        position = self.get_start_position()
        self.draw_map(position[0], position[1], self.dungeon)

    def render_biome(self):
        """ Method for rendering the biome
        """
        if self.biome is None:
            return
        position = self.get_start_position()
        self.draw_map(position[0], position[1], self.biome)

    def draw_map(self, start_x, start_y, map_type):
        """ Method for drawing the map on canvas
        """
        for y in range(self.height):
            for x in range(self.width):
                pos_x = start_x + x * self.block_size
                pos_y = start_y + y * self.block_size
                if map_type[x][y] == "#" or map_type[x][y] == "*":
                    color = colors["#"]
                else:
                    color = colors["."]
                pygame.draw.rect(self.screen, color, (pos_x-20, pos_y, self.block_size, self.block_size))

    def get_start_position(self):
        """ Method which decides where to start drawing
            the map on the canvas
        Returns:
            tuple: integers x, y
        """
        screen_center_x = self.screen.get_width() // 2
        screen_center_y = self.screen.get_height() // 2
        start_x = screen_center_x - self.width * self.block_size // 2
        start_y = screen_center_y - self.height * self.block_size // 2
        return start_x, start_y

    def increase_maximum_room_size_slider(self):
        """ Helper method to make sure that the value of
            minimum slider can never be greater than maximum"""
        self.max_room_size_slider.current_value = self.min_room_size + 1
        self.max_room_size_slider.draw_all(self.screen, self.slider_font)
        self.max_room_size = self.max_room_size_slider.current_value
