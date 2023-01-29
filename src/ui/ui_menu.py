import pygame

class Menu:

    """This class functions as the main loop menu for the UI
    """

    def __init__(self):
        self.running = True

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_menu()

    def exit_menu(self):
        self.running = False
