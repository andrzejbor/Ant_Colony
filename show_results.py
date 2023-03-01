import pygame.font


class ShowResults:
    """Class created to show algorithm results"""

    def __init__(self, ac_prog):
        """Initialization results attribute"""
        self.ac_prog = ac_prog
        self.screen = self.ac_prog.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.ac_prog.settings
        self.stats = self.ac_prog.stats

        # Results text settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial results
        self.prep_best_result()

    def prep_best_result(self):
        """Conversion best result to image"""
        result_str = "{:,}".format(self.stats.best_way_length)
        self.result_image = self.font.render(result_str, True,
                                             self.text_color, self.settings.bg_color)
        # Display best result in middle top of screen
        self.result_rect = self.result_image.get_rect()
        self.result_rect.centerx = self.screen_rect.centerx
        self.result_rect.top = self.screen_rect.top

    def show_result(self):
        """Show best result"""
        self.screen.blit(self.result_image, self.result_rect)