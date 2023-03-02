import sys
import time
import pygame
from random import randrange
from settings import Settings
from city import City
from road import Road
from prog_stats import ProgStats
from ant import Ant
from show_results import ShowResults
from state_machine import ProgramState
from program_menu import ProgramMenu


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

        self.sr = ShowResults(self)
        self.prog_menu = ProgramMenu(self)

        self.prog_stat = ProgramState()

        self.cities = pygame.sprite.Group()
        self.roads = pygame.sprite.Group()
        self.ants = pygame.sprite.Group()

        self._create_cities()
        self._create_roads()
        self._choose_start_city()
        self._create_ants()

    def run_program(self):
        """Run main loop"""
        while True:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            self._refresh_roads()
            self._update_ants()
            self._update_screen()
            self._program_sleep()

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
                city.rect.x = randrange(self.settings.screen_left_border,
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
        random_index = randrange(len(self.cities.sprites()))
        self.stats.start_city = self.cities.sprites()[random_index]
        self.cities.sprites()[random_index].change_start_city_color()

    def _create_ants(self):
        """Create ants"""
        for ant_number in range(self.settings.ant_limit):
            ant = Ant(self, ant_number)
            self.ants.add(ant)

    def _move_ants(self):
        """If journey not completed - move ants"""
        self.stats.ant_moving_phase = True
        for ant in self.ants:
            if not ant.journey_compleat:
                ant.go_to_next_city()
            else:
                self.stats.iteration_complete = True

    def _refresh_roads(self):
        """refresh roads ti initial color"""
        for road in self.roads:
            road.back_to_initial_road_settings()

    def _update_ants(self):
        """Managing ants. Move ants as long as iteration is not compleat.
        Show each ant traveled road after iteration end, then reset iteration"""

        if not self.stats.iteration_complete:
            self._move_ants()
        else:
            # Check program state
            if self.prog_stat.ant_move_state.is_active:
                self.prog_stat.switch_to_show_result()

            # Show each ant result
            for ant in self.ants:
                if ant.journey_compleat:
                    ant.color_traveled_roads()
                    ant.journey_compleat = False
                    self.stats.current_ant_result = ant.distance_traveled
                    self.stats.current_ant_number = ant.ant_number
                    self.sr.prep_ant_result()
                    return
            self.stats.iteration_complete = False
            self._search_for_best_way()
            self._reset_ants_for_next_iteration()
            self.prog_stat.switch_to_ant_move()

    def _reset_ants_for_next_iteration(self):
        """Reset ants before next iteration"""
        self.ants.empty()
        self._create_ants()

    def _program_sleep(self):
        """Manage pause time for better showing result"""
        if self.prog_stat.ant_move_state.is_active:
            time.sleep(self.settings.ant_move_delay)
        elif self.prog_stat.show_results_state.is_active:
            time.sleep(self.settings.show_traveled_roads_delay)

    def _search_for_best_way(self):
        """Check all traveled way in this iteration and save best one"""
        if self.stats.best_way_length == 0:
            self.stats.best_way_length = self.ants.sprites()[0].distance_traveled
            self.stats.best_way = self.ants.sprites()[0].visited_cities
        for ant in self.ants:
            if ant.distance_traveled < self.stats.best_way_length:
                self.stats.best_way_length = ant.distance_traveled
                self.stats.best_way = ant.visited_cities
        self.sr.prep_best_result()

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

        # Show best result
        self.sr.show_result()

        # Show menu
        self.prog_menu.display_menu()

        # Display last refresh screen
        pygame.display.flip()


if __name__ == '__main__':
    ac = AntColony()
    ac.run_program()
