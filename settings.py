import pygame.font


class Settings:
    """Class for storage all settings"""

    def __init__(self):
        """Initialization program settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_border = 100
        self.screen_left_border = 200

        # City settings
        self.city_number = 5
        self.city_color = (0, 0, 0)
        self.city_size = 20
        self.city_border = 100
        self.start_city_color = (250, 250, 0)

        # Road settings
        self.road_color = (250, 0, 0)
        self.road_width = 2

        # Ant settings
        self.ant_limit = 5
        self.ant_road_color = (0, 0, 250)
        self.ant_road_width = 4

        # Time settings
        self.ant_move_delay = 0.5
        self.show_traveled_roads_delay = 1.5
        self.ant_move_delay_long = 0.5
        self.show_traveled_roads_delay_long = 1.5
        self.ant_move_delay_short = 0.1
        self.show_traveled_roads_delay_short = 0.3

        # Program end settings
        self.iteration_without_better_result_limit = 2

        # Menu settings
        self.menu_width = 200
        self.menu_color = (0, 0, 0)

        # Button settings
        self.button_width = 150
        self.button_high = 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.distance_from_left = 25
        self.distance_between_buttons = 30

        # Start button
        self.start_button_number = 0
        self.start_button_text = "Start"

        # Restart algorithm button
        self.restart_button_number = 1
        self.restart_button_text = "Restart"

        # Quick version button
        self.speedup_button_number = 2
        self.speedup_button_text = "Quick"

        # Slow version button
        self.slowdown_button_number = 3
        self.slowdown_button_text = "Slow"

        # Brute force button
        self.bruteforce_button_number = 4
        self.bruteforce_button_text = "BF"

        # Brute force result "button"
        self.bf_result_number = 5
