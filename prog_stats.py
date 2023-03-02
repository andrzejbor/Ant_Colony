class ProgStats:
    """Class for storage all program statistic"""

    def __init__(self):
        self.start_city = None

        # Current ant results
        self.current_ant_result = 0
        self.current_ant_number = 0

        self.restart_stats()

    def restart_stats(self):
        """Reset stats"""
        self.best_way_length = 0
        self.best_way = []
        self.iteration_complete = False
        self.iteration_without_better_result = 0
