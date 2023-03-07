from random import randrange
import pygame
from pygame.sprite import Sprite


class Ant(Sprite):
    """Class for managing ants"""

    def __init__(self, ac_prog, ant_number):
        super().__init__()
        self.ac_prog = ac_prog
        self.screen = ac_prog.screen
        self.settings = ac_prog.settings
        self.city_to_visit = ac_prog.cities.copy()
        self.roads = ac_prog.roads
        self.possible_roads = self.roads.copy()
        self.start_city = ac_prog.stats.start_city
        self.current_position = self.start_city
        self.visited_cities = pygame.sprite.Group()
        self.traveled_roads = pygame.sprite.Group()
        self.distance_traveled = 0
        self.journey_compleat = False
        self.ant_number = ant_number

    def go_to_next_city(self):
        """Move to next city as long as all cities will be visited. After that move to start city"""
        self.visited_cities.add(self.current_position)
        self.city_to_visit.remove(self.current_position)
        if len(self.city_to_visit) > 0:
            self.current_position = self._choose_next_city()
        else:
            self.current_position = self.start_city
            self.journey_compleat = True
        last_road = self._find_last_road()
        last_road.mark_traveled_road()
        last_road.add_ant_pheromone()
        self.traveled_roads.add(last_road)
        self.distance_traveled += last_road.road_length

    def _choose_next_city(self):
        """Choose next city to visit. There is bigger chance to choose closer city"""
        possible_roads_from_current_city = self.current_position.find_possible_roads_from_city(self.possible_roads)
        for possible_road in possible_roads_from_current_city:
            self.possible_roads.remove(possible_road)
        chosen_road = self._fortune_wheel(possible_roads_from_current_city)
        return chosen_road.find_city_at_end_fo_road(self.current_position)

    def _fortune_wheel(self, roads):
        """Choose city in fortune wheel (shorter road and road with pheromone has bigger chance)"""
        fortune_wheel = []
        for road in roads:
            for number in range(self.ac_prog.stats.road_limit - road.road_length):
                fortune_wheel.append(road)
            for number in range(road.ant_pheromone):
                fortune_wheel.append(road)
        return fortune_wheel[randrange(len(fortune_wheel))]

    def _find_last_road(self):
        """Find last traveled road"""
        for road in self.roads:
            if road.pos_1 == self.visited_cities.sprites()[-1].rect.center \
                    and road.pos_2 == self.current_position.rect.center:
                return road
            elif road.pos_2 == self.visited_cities.sprites()[-1].rect.center \
                    and road.pos_1 == self.current_position.rect.center:
                return road

    def color_traveled_roads(self):
        """Change color for all traveled roads"""
        for road in self.traveled_roads:
            road.mark_traveled_road()
