import pygame
from pygame.sprite import Sprite


class City(Sprite):
    """Class showing one citi"""

    def __init__(self, ac_prog):
        """Initialization city and define it position"""

        super().__init__()
        self.ac_prog = ac_prog
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.color = self.settings.city_color

        # Create city at (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.city_size,
                                self.settings.city_size)

    def change_start_city_color(self):
        self.color = self.settings.start_city_color

    def find_possible_roads_from_city(self, roads):
        """From given roads pool, find possible roads from this city"""
        possible_roads = []
        for road in roads:
            road_ends = [road.pos_1, road.pos_2]
            if self.rect.center in road_ends:
                possible_roads.append(road)
        return possible_roads

    def draw_city(self):
        """Display city on screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)
