class BruteForce:
    """Class for find the best way in brute force method"""

    def __init__(self, ac_prog):
        self.ac_prog = ac_prog
        self.stats = self.ac_prog.stats
        self.cities_to_visit = self.ac_prog.cities.copy()
        self.roads = self.ac_prog.roads
        self.best_way_length = 0
        self.best_way = []

    def _get_selected_road(self, city, next_city):
        """Find selected road and return it length"""
        for road in self.roads:
            road_ends = [road.pos_1, road.pos_2]
            if city.rect.center in road_ends and next_city.rect.center in road_ends:
                return road

    def _summary_way_length(self, city, sum_length, all_roads, traveled_roads=[]):
        """Summary length for each road"""
        if len(all_roads) > 0:
            all_roads_copy = all_roads.copy()
            possible_roads = city.find_possible_roads_from_city(all_roads_copy)
            for road in possible_roads:
                all_roads_copy.remove(road)
            for road in possible_roads:
                traveled_roads_copy = traveled_roads.copy()
                traveled_roads_copy.append(road)
                next_city = road.find_city_at_end_fo_road(city)
                self._summary_way_length(next_city, sum_length + road.road_length, all_roads_copy, traveled_roads_copy)
        else:
            # Add way to start city
            last_road = self._get_selected_road(city, self.stats.start_city)
            sum_length += last_road.road_length
            traveled_roads.append(last_road)
            if self.best_way_length == 0 or self.best_way_length > sum_length:
                self.best_way_length = sum_length
                self.best_way = traveled_roads

    def find_best_way_brute_force(self):
        """Run brute force algorithm"""
        self.cities_to_visit.remove(self.stats.start_city)
        self._summary_way_length(self.stats.start_city, 0, self.roads)
        self.stats.brute_force_way = self.best_way
