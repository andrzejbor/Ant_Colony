class ProgStats:
    """Class for storage all program statistic"""

    def __init__(self):
        # Best way stats
        self.best_way_length = 0
        self.best_way = []
        self.start_city = None
        self.iteration_complete = False

        # Current ant results
        self.current_ant_result = 0
        self.current_ant_number = 0

    def restart_stats(self):
        """Reset stats"""
        self.best_way_length = 0
        self.best_way = []
        self.start_city = None
        self.iteration_complete = False
