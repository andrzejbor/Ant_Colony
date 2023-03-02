import pygame


class ProgramMenu:
    """Class displayed and manage program menu"""

    def __init__(self, ac_prog):
        """Initialization manu attributes """
        self.ac_prog = ac_prog
        self.screen = ac_prog.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.ac_prog.settings
        self.rect = pygame.Rect(0, 0, self.settings.menu_width,
                                self.settings.screen_height)

    def draw_menu_rect(self):
        """Draw menu rect on the screen"""

        pygame.draw.rect(self.screen, self.settings.menu_color, self.rect)

    def display_menu(self):
        """Display all manu element on screen"""
        self.draw_menu_rect()
