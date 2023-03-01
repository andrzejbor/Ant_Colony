import pygame.font


class ShowResults:
    """Class created to show algoritm results"""

    def __init__(self, ac_prog):
        """Inicialization results atribute"""
        self.ac_prog = ac_prog
        self.screen = self.ac_prog.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.ac_prog.settings
        self.stats = self.ac_prog.stats

        # Results text settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial results
        pass
