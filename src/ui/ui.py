import pygame
from ui.ui_menu import Menu

WIDTH = 1200
HEIGHT = 1000

class UI:

    """This class functions as a base user interface for the program
    """

    def __init__(self):

        self.draw_screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.caption = pygame.display.set_caption("Dungeon Generator")
        self.menu = Menu()

        pygame.init()
