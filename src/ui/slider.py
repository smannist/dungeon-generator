import pygame

class Slider:
    """ A slider class for the UI
        The goal is to clear the slider each time the slider circle is moved
    
    Args:
        x (int): slider start x-position
        y (int): slider start y-position
        width (int): slider width
        min_value (int): minimum value the slider can take
        max_value (int): maximum value the slider can take
        current_value (int): start / current value of the slider
        slider_bar_color (rbg): the color of the slider background bar
        text (string): slider text
    """
    def __init__(self, x, y, width, min_value, max_value, current_value, slider_bar_color, text):
        self.x = x
        self.y = y
        self.width = width
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value
        self.slider_bar_color = slider_bar_color
        self.text = text
        self.circle_radius = 15
        self.circle_x = self.value_to_position(current_value)
        self.rect = pygame.Rect(x, y - self.circle_radius // 2, width, self.circle_radius)

    def draw_all(self, screen, font):
        """Method for drawing the whole slider on the canvas
        """
        self.clear_slider_bar(screen)
        self.clear_value_text_background(screen)
        self.draw_text(screen, font)
        self.draw_slider_line(screen)
        self.draw_slider_circle(screen)
        self.draw_value_text(screen, font)

    def clear_slider_bar(self, screen):
        """Method for clearing the state of slider bard
        """
        bar_clear_rect = pygame.Rect(self.x - self.circle_radius, self.y - self.circle_radius, \
                                 self.width + 2 * self.circle_radius, 2 * self.circle_radius + 1)
        pygame.draw.rect(screen, self.slider_bar_color, bar_clear_rect)

    def clear_value_text_background(self, screen):
        """Method for clearing the state of slider value text
        """
        text_clear_rect = pygame.Rect(self.x, self.y - self.circle_radius, self.width, 50)
        pygame.draw.rect(screen, self.slider_bar_color, text_clear_rect)

    def draw_text(self, screen, font):
        """Method for drawing the main text of the slider
        """
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y - self.circle_radius - 10))
        screen.blit(text_surface, text_rect)

    def draw_slider_line(self, screen):
        """Method for drawing the slider line
        """
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 5)

    def draw_slider_circle(self, screen):
        """Method for drawing slider circle
        """
        circle_x = self.value_to_position(self.current_value)
        circle_y = self.y
        pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), self.circle_radius)

    def draw_value_text(self, screen, font):
        """Method for drawing the current value of slider
        """
        value_str = str(self.current_value)
        value_text = font.render(value_str, True, (255, 255, 255))
        value_rect = value_text.get_rect(center=(self.x + self.width // 2, self.y + self.circle_radius + 10))
        pygame.draw.rect(screen, self.slider_bar_color, value_rect)
        screen.blit(value_text, value_rect)

    def update_current_value(self, mouse_pos, mouse_pressed):
        """Method for updating the state of current value
        """
        if mouse_pressed[0] == 1:
            self.circle_x = mouse_pos[0]
            if self.circle_x < self.x:
                self.circle_x = self.x
            elif self.circle_x > self.x + self.width:
                self.circle_x = self.x + self.width
            self.current_value = int(self.position_to_value(self.circle_x) + 0.5)

    def collidepoint(self, mouse_pos):
        """Method for checking if the mouse is positioned at the slider
        """
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def value_to_position(self, value):
        """Method for translating the value to position
        """
        return int((value - self.min_value) / (self.max_value - self.min_value) * self.width) + self.x

    def position_to_value(self, pos):
        """Method for translating the position to value
        """
        return (pos - self.x) / self.width * (self.max_value - self.min_value) + self.min_value
