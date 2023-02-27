import sys
import pygame
from random import randrange
from settings import Settings
from city import City


class AntColony:
    """Main class"""

    def __init__(self):
        """Program initialization"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ant Colony")

        self.cities = pygame.sprite.Group()

        self._create_cities()

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
            city.rect.x = randrange(self.settings.screen_width - 20)
            city.rect.y = randrange(self.settings.screen_height - 20)
            self.cities.add(city)

            print(f"Nowe miasto x = {city.rect.x}, y = {city.rect.y}")

    def _update_screen(self):
        """Refresh object on screen"""
        # Refresh screen in every iteration
        self.screen.fill(self.settings.bg_color)

        # Draw cities
        for city in self.cities:
            city.draw_city()

        # Display last refresh screen
        pygame.display.flip()


if __name__ == '__main__':
    ac = AntColony()
    ac.run_program()
