class ButtonEvents:
    """Class for storage logic of button events"""

    def __init__(self, ac_prog):
        self.ac_prog = ac_prog
        self.prog_stat = self.ac_prog.prog_stat

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
        elif self.prog_stat.ant_move_state.is_active or self.prog_stat.show_results_state.is_active:
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

            if self.prog_stat.current_state.id == "ant_move_state":
                self.prog_stat.from_ant_to_pause()
            else:
                self.prog_stat.from_show_to_pause()
