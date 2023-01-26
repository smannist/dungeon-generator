import pygame

class Menu:

    """This class functions as the main loop menu for the UI
    """

    def __init__(self):
        self.running = True

    def menu_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_loop()

    def exit_loop(self):
        self.running = False
