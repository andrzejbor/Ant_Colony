import pygame
from pygame.sprite import Sprite


class Ant(Sprite):
    """Class for managing ants"""

    def __init__(self, ac_prog):
        super().__init__()
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.city_to_visit = ac_prog.cities
        self.current_position = None
        self.visited_cities = []
        self.distance_traveled = 0
