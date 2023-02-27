import sys
import pygame


class AntColony:
    """Main class"""

    def __init__(self):
        """Program initialization"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Ant Colony")

    def run_program(self):
        """Run main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((230, 230, 230))
            pygame.display.flip()


if __name__ == '__main__':
    ac = AntColony()
    ac.run_program()
