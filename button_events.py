from brute_force import BruteForce
class ButtonEvents:
    """Class for storage logic of button events"""

    def __init__(self, ac_prog):
        self.ac_prog = ac_prog
        self.prog_stat = self.ac_prog.prog_stat
        self.settings = self.ac_prog.settings
        self.stats = self.ac_prog.stats

    def click_start_button(self):
        """Start program if no started"""
        if self.prog_stat.initial_state.is_active:
            self.prog_stat.start_program()
        elif self.prog_stat.pause_state.is_active:
            self.prog_stat.restart_program()

    def click_restart_button(self, ac_prog):
        """Reset cities, roads and result. Change state to pause"""
        if self.prog_stat.initial_state.is_active:
            pass
        elif self.prog_stat.ant_move_state.is_active \
                or self.prog_stat.show_results_state.is_active \
                or self.prog_stat.end_program_state.is_active:
            # Delete old cities, roads and ants
            ac_prog.cities.empty()
            ac_prog.roads.empty()
            ac_prog.ants.empty()

            # Create new ones
            ac_prog._create_cities()
            ac_prog._create_roads()
            ac_prog._choose_start_city()
            ac_prog._create_ants()

            ac_prog.stats.restart_stats()
            ac_prog.sr.prep_best_result()

            if self.prog_stat.current_state.id == "ant_move_state":
                self.prog_stat.from_ant_to_pause()
            elif self.prog_stat.current_state.id == "show_results_state":
                self.prog_stat.from_show_to_pause()
            elif self.prog_stat.current_state.id == "end_program_state":
                self.prog_stat.from_end_to_pause()

    def click_speedup_button(self):
        """Change delay for shorter version"""
        self.settings.ant_move_delay = self.settings.ant_move_delay_short
        self.settings.show_traveled_roads_delay = self.settings.show_traveled_roads_delay_short

    def click_slowdown_button(self):
        """Change delay for long version"""
        self.settings.ant_move_delay = self.settings.ant_move_delay_long
        self.settings.show_traveled_roads_delay = self.settings.show_traveled_roads_delay_long

    def click_brute_force_button(self):
        """Run brute force algorithm and show result"""
        bf = BruteForce(self.ac_prog)
        bf.find_best_way_brute_force()
        self.stats.brute_force_result = bf.best_way
        print(bf.best_way)
        self.ac_prog.stats.show_brute_force_result = True
