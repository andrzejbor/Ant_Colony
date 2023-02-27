import pygame
from pygame.sprite import Sprite


class City(Sprite):
    """Class showing one citi"""

    def __init__(self, ac_prog):
        """Initialization city and define it position"""
        super().__init__()
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.color = self.settings.city_color

        # Create city at (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.city_size,
                                self.settings.city_size)

    def draw_city(self):
        """Display city on screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)
