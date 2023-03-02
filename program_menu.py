import pygame
from button import Button


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

    def draw_start_button(self):
        """Draw start button"""
        self.start_button = Button(self.ac_prog, self.settings.start_button_text,
                              self.settings.start_button_number)
        self.start_button.draw_button()

    def display_menu(self):
        """Display all manu element on screen"""
        self.draw_menu_rect()
        self.draw_start_button()
