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
from button_events import ButtonEvents


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
        self.bt_events = ButtonEvents(self)

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
            self._update_roads_and_ants()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def _check_buttons(self, mouse_pos):
        """Check if one of buttons was clic"""
        if self.prog_menu.start_button.rect.collidepoint(mouse_pos):
            self.bt_events.click_start_button()
        elif self.prog_menu.restart_button.rect.collidepoint(mouse_pos):
            self.bt_events.click_restart_button(self)
        elif self.prog_menu.speedup_button.rect.collidepoint(mouse_pos):
            self.bt_events.click_speedup_button()
        elif self.prog_menu.slowdown_button.rect.collidepoint(mouse_pos):
            self.bt_events.click_slowdown_button()

    def _create_cities(self):
        """Creates all cities"""
        create_cities_not_compleat = True
        while create_cities_not_compleat:
            for city_number in range(self.settings.city_number):
                city = City(self)
                create_success = False
                for number in range(10):
                    city.rect.x = randrange(self.settings.screen_left_border,
                                            self.settings.screen_width - self.settings.screen_border)
                    city.rect.y = randrange(self.settings.screen_border,
                                            self.settings.screen_height - self.settings.screen_border)
                    if self._check_is_city_near(city):
                        # Have to random new position
                        pass
                    else:
                        create_success = True
                        break
                if create_success:
                    self.cities.add(city)
                else:
                    # Empty cities list and start creating from beginning
                    self.cities.empty()
                    break
            if len(self.cities) == self.settings.city_number:
                break

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
            if self._check_end_program_condition():
                pass
            else:
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
        better_result_found = False
        if self.stats.best_way_length == 0:
            self.stats.best_way_length = self.ants.sprites()[0].distance_traveled
            self.stats.best_way = self.ants.sprites()[0].traveled_roads
        for ant in self.ants:
            if ant.distance_traveled < self.stats.best_way_length:
                self.stats.best_way_length = ant.distance_traveled
                self.stats.best_way = ant.traveled_roads
                better_result_found = True
        self.sr.prep_best_result()
        if better_result_found:
            self.stats.iteration_without_better_result = 0
        else:
            self.stats.iteration_without_better_result += 1

    def _check_end_program_condition(self):
        """Check if end program condition has been met"""
        if self.stats.iteration_without_better_result >= self.settings.iteration_without_better_result_limit:
            self.prog_stat.switch_to_end()
            return True
        return False

    def _update_roads_and_ants(self):
        """Update, or not, roads and ants depending on state"""
        if self.prog_stat.initial_state.is_active or self.prog_stat.pause_state.is_active:
            pass
        elif self.prog_stat.ant_move_state.is_active or self.prog_stat.show_results_state.is_active:
            self._refresh_roads()
            self._update_ants()
        elif self.prog_stat.end_program_state.is_active:
            self._refresh_roads()
            self._show_best_way()

    def _show_best_way(self):
        """Show best founded way"""
        best_ant = Ant(self, 1)
        best_ant.traveled_roads = self.stats.best_way
        best_ant.color_traveled_roads()

    def _update_screen(self):
        """Refresh object on screen"""
        # Refresh screen in every iteration
        self.screen.fill(self.settings.bg_color)

        if not self.prog_stat.initial_state.is_active:
            # Draw roads, cities and best result
            for road in self.roads:
                road.draw_road()
            for city in self.cities:
                city.draw_city()
            self.sr.show_result()

        # Show menu
        self.prog_menu.display_menu()

        # Display last refresh screen
        pygame.display.flip()


if __name__ == '__main__':
    ac = AntColony()
    ac.run_program()
