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
        self.prep_ant_result()

    def prep_best_result(self):
        """Conversion best result to image"""
        result_str = "Best results = " + "{:,}".format(self.stats.best_way_length)
        self.result_image = self.font.render(result_str, True,
                                             self.text_color, self.settings.bg_color)
        # Display best result in left top of screen
        self.result_rect = self.result_image.get_rect()
        self.result_rect.left = self.settings.screen_width // 8
        self.result_rect.top = self.screen_rect.top + 10

    def prep_ant_result(self):
        """Conversion ant result to image"""
        ant_res_str = f"Ant_{self.stats.current_ant_number} result = " \
                      + "{:,}".format(self.stats.current_ant_result)
        self.ant_res_image = self.font.render(ant_res_str, True,
                                              self.text_color, self.settings.bg_color)
        # Display best result in right top of screen
        self.ant_res_rect = self.ant_res_image.get_rect()
        self.ant_res_rect.right = self.screen_rect.right - self.settings.screen_width // 8
        self.ant_res_rect.top = self.screen_rect.top + 10

    def show_result(self):
        """Show best result and ant result"""
        self.screen.blit(self.result_image, self.result_rect)
        if self.stats.iteration_complete:
            self.screen.blit(self.ant_res_image, self.ant_res_rect)
