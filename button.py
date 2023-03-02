import pygame.font

class Button:
    """Class for create buttons"""

    def __init__(self, ac_prog, top_left_pos, button_text):
        """Initialization button attribute"""
        self.ac_prog = ac_prog
        self.screen = self.ac_prog.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.ac_prog.settings

        # Define button size and attributes
        self.width = self.settings.button_width
        self.height = self.settings.button_high
        self.button_color = self.settings.button_color
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.SysFont(None, 48)

        # Create button rect and put it in proper place
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = top_left_pos

        self.text = button_text

    def _prep_text(self):
        """Convert button text to image and put it in center"""
        self.text_image = self.font.render(self.text, True, self.text_color,
                                           self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        """Display button on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)