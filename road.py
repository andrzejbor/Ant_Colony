import math
import pygame
from pygame.sprite import Sprite


class Road(Sprite):
    """Class showing one road between cities"""

    def __init__(self, ac_prog, city_1, city_2):
        """Initialization road and calculate it length"""
        super().__init__()
        self.ac_prog = ac_prog
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.color = self.settings.road_color
        self.width = self.settings.road_width
        self.pos_1 = city_1.rect.center
        self.pos_2 = city_2.rect.center
        self.road_length = self._calculate_road_length(self.pos_1, self.pos_2)
        self.ant_pheromone = 0

    def _calculate_road_length(self, pos_1, pos_2):
        """Calculate distance between two cities"""
        return int(math.sqrt(math.pow(abs(pos_1[0] - pos_2[0]), 2)
                             + math.pow(abs(pos_1[1] - pos_2[1]), 2)))

    def mark_traveled_road(self):
        """Change road color to blue"""
        self.color = self.settings.ant_road_color
        self.width = self.settings.ant_road_width

    def back_to_initial_road_settings(self):
        """Change road color to initial"""
        self.color = self.settings.road_color
        self.width = self.settings.road_width

    def draw_road(self):
        """Display road on the screen"""
        pygame.draw.line(self.screen, self.color, self.pos_1, self.pos_2, self.width)

    def find_city_at_end_fo_road(self, city):
        """Find city at the other end of road then provided city"""
        if self.pos_1 == city.rect.center:
            second_city_pos = self.pos_2
        else:
            second_city_pos = self.pos_1
        for possible_city in self.ac_prog.cities:
            if possible_city.rect.center == second_city_pos:
                return possible_city

    def add_ant_pheromone(self):
        """Add pheromone. Quantity depend on road long (shorter get more)"""
        self.ant_pheromone += int(((self.ac_prog.stats.road_limit - self.road_length)
                                   * self.settings.ant_pheromone_quantity_percent) / 100)

    def evaporation_pheromone(self):
        """Evaporate pheromone from roads after ant iteration"""
        self.ant_pheromone = int(self.ant_pheromone * self.settings.ant_pheromone_evaporation_percent / 100)

    def draw_brute_force_road(self):
        """Draw road for bruteforce algorithm"""
        pygame.draw.line(self.screen, self.settings.brute_force_color, self.pos_1, self.pos_2,
                         self.settings.brute_force_width)
