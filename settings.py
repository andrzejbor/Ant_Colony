class Settings:
    """Class for storage all settings"""

    def __init__(self):
        """Initialization program settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_border = 100

        # City settings
        self.city_number = 5
        self.city_color = (0, 0, 0)
        self.city_size = 20
        self.city_border = 100
        self.start_city_color = (250, 250, 0)

        # Road settings
        self.road_color = (250, 0, 0)

        # Ant settings
        self.ant_limit = 1
        self.ant_road_color = (0, 0, 250)
