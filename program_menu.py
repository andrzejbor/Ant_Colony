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

    def draw_restart_button(self):
        """Draw restart button"""
        self.restart_button = Button(self.ac_prog, self.settings.restart_button_text,
                                     self.settings.restart_button_number)
        self.restart_button.draw_button()

    def draw_speedup_button(self):
        """Draw speedup button"""
        self.speedup_button = Button(self.ac_prog, self.settings.speedup_button_text,
                                     self.settings.speedup_button_number)
        self.speedup_button.draw_button()

    def draw_slowdown_button(self):
        """Draw slowdown button"""
        self.slowdown_button = Button(self.ac_prog, self.settings.slowdown_button_text,
                                      self.settings.slowdown_button_number)
        self.slowdown_button.draw_button()

    def display_menu(self):
        """Display all manu element on screen"""
        self.draw_menu_rect()
        self.draw_start_button()
        self.draw_restart_button()
        self.draw_speedup_button()
        self.draw_slowdown_button()
