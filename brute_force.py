class BruteForce:
    """Class for find the best way in brute force method"""

    def __init__(self, ac_prog):
        self.ac_prog = ac_prog
        self.stats = self.ac_prog.stats
        self.cities_to_visit = self.ac_prog.cities
        self.roads = self.ac_prog.roads
        self.best_way = 0

    def _find_all_roads_from_city(self, city, roads):
        """Find all possible roads from selected city"""
        possible_roads = []
        for road in roads:
            road_ends = [road.pos_1, road.pos_2]
            if city.rect.center in road_ends:
                possible_roads.append(road)
        return possible_roads

    def _find_city_at_end_of_road(self, road, city):
        """Find second city in selected road"""
        if road.pos_1 == city.rect.center:
            second_city_pos = road.pos_1
        else:
            second_city_pos = road.pos_2
        for city in self.ac_prog.cities:
            if city.rect.center == second_city_pos:
                return city

    def _get_selected_road_length(self, city, next_city, roads):
        """Find selected road and return it length"""
        for road in roads:
            road_ends = [road.pos_1, road.pos_2]
            if city.rect.center in road_ends and next_city.rect.center in road_ends:
                return road.road_length

    def _summary_way_length(self, city, sum_length, all_roads):
        """Summary length for each road"""
        if len(all_roads) > 0:
            all_roads_copy = all_roads.copy()
            possible_roads = self._find_all_roads_from_city(city, all_roads_copy)
            for road in possible_roads:
                all_roads_copy.remove(road)
            for road in possible_roads:
                next_city = self._find_city_at_end_of_road(road, city)
                self._summary_way_length(next_city, sum_length + road.road_length, all_roads_copy)
        else:
            if self.best_way == 0 or self.best_way > sum_length:
                self.best_way = sum_length



    def find_best_way_brute_force(self):
        """Run brute force algorithm"""
        self.current_city = self.stats.start_city
        self.cities_to_visit.remove(self.current_city)

        for city in self.cities_to_visit:
            self._summary_way_length(city, 0, self.roads)

        print(self.best_way)