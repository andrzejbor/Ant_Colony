import sys
import pygame
from settings import Settings


class AntColony:
    """Main class"""

    def __init__(self):
        """Program initialization"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ant Colony")

    def run_program(self):
        """Run main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            # Display last refresh screen
            pygame.display.flip()


if __name__ == '__main__':
    ac = AntColony()
    ac.run_program()
