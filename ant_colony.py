import sys
import pygame
from random import randrange
from settings import Settings
from city import City
from road import Road
from prog_stats import ProgStats
from ant import Ant


class AntColony:
    """Main class"""

    def __init__(self):
        """Program initialization"""
        pygame.init()
        self.settings = Settings()
        self.stats = ProgStats()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ant Colony")

        self.cities = pygame.sprite.Group()
        self.roads = pygame.sprite.Group()
        self.ants = pygame.sprite.Group()

        self._create_cities()
        self._create_roads()
        self._create_ants()

    def run_program(self):
        """Run main loop"""
        while True:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            self._update_screen()

    def _check_events(self):
        """Reaction for mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_cities(self):
        """Creates all cities"""
        for city_number in range(self.settings.city_number):
            city = City(self)
            while True:
                city.rect.x = randrange(self.settings.screen_border,
                                        self.settings.screen_width - self.settings.screen_border)
                city.rect.y = randrange(self.settings.screen_border,
                                        self.settings.screen_height - self.settings.screen_border)
                if self._check_is_city_near(city):
                    # Have to random new position
                    pass
                else:
                    break

            self.cities.add(city)

    def _check_is_city_near(self, new_city):
        """Check is any other city inside city border"""
        for city in self.cities:
            if abs(city.rect.x - new_city.rect.x) < self.settings.city_border or \
                    abs(city.rect.y - new_city.rect.y) < self.settings.city_border:
                return True
        return False

    def _create_roads(self):
        """Create roads between all cities"""
        cities_copy = self.cities.copy()
        for city in self.cities:
            for city_copy in cities_copy:
                if self._check_cities_position(city, city_copy):
                    continue
                else:
                    road = Road(self, city, city_copy)
                    self.roads.add(road)
            cities_copy.remove(city)

    def _check_cities_position(self, city_1, city_2):
        """Check if two cities is in the same position"""
        return city_1.rect.center == city_2.rect.center

    def _choose_start_city(self):
        """Draw random city as start"""
        self.stats.start_city = self.cities[range(len(self.cities))]

    def _create_ants(self):
        for ant_number in range(self.settings.ant_limit):
            ant = Ant(self)
            self.ants.add(ant)
        print(len(self.ants))

    def _update_screen(self):
        """Refresh object on screen"""
        # Refresh screen in every iteration
        self.screen.fill(self.settings.bg_color)

        # Draw roads
        for road in self.roads:
            road.draw_road()

        # Draw cities
        for city in self.cities:
            city.draw_city()

        # Display last refresh screen
        pygame.display.flip()


if __name__ == '__main__':
    ac = AntColony()
    ac.run_program()
