import math
import pygame
from pygame.sprite import Sprite


class Road(Sprite):
    """Class showing one road between cities"""

    def __init__(self, ac_prog, city_1, city_2):
        """Initialization road and calculate it length"""
        super().__init__()
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.color = self.settings.road_color
        self.pos_1 = city_1.rect.center
        self.pos_2 = city_2.rect.center
        self.road_length = self._calculate_road_length(self.pos_1, self.pos_2)

    def _calculate_road_length(self, pos_1, pos_2):
        """Calculate distance between two cities"""
        return int(math.sqrt(math.pow(abs(pos_1[0] - pos_2[0]), 2)
                             + math.pow(abs(pos_1[1] - pos_2[1]), 2)))

    def draw_road(self):
        """Display road on the screen"""

        pygame.draw.line(self.screen, self.color, self.pos_1, self.pos_2)
