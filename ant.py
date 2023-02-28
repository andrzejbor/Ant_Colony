from random import randrange
import pygame
from pygame.sprite import Sprite


class Ant(Sprite):
    """Class for managing ants"""

    def __init__(self, ac_prog):
        super().__init__()
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.city_to_visit = ac_prog.cities.copy()
        self.roads = ac_prog.roads
        self.current_position = ac_prog.stats.start_city
        self.visited_cities = pygame.sprite.Group()
        self.distance_traveled = 0
        self.journey_compleat = False

    def go_to_next_city(self):
        """Move to next city"""
        if len(self.city_to_visit) > 1:
            self.visited_cities.add(self.current_position)
            self.city_to_visit.remove(self.current_position)
            self.current_position = self._choose_random_city()
            last_road = self._find_last_road()
            last_road.change_color()
            self.distance_traveled += last_road.road_length
        else:
            # TODO have to change to - move to last city and move to start. After that loop will be complete
            # Move to start city
            self.visited_cities.add(self.current_position)
            self.current_position = self.city_to_visit.sprites()[0]
            self.visited_cities.add(self.current_position)
            self.journey_compleat = True

    def _choose_random_city(self):
        """Draw random city from not visited"""
        return self.city_to_visit.sprites()[randrange(len(self.city_to_visit.sprites()))]

    def _find_last_road(self):
        """Find last traveled road"""
        for road in self.roads:
            if road.pos_1 == self.visited_cities.sprites()[-1].rect.center \
                    and road.pos_2 == self.current_position.rect.center:
                return road
            elif road.pos_2 == self.visited_cities.sprites()[-1].rect.center \
                    and road.pos_1 == self.current_position.rect.center:
                return road
