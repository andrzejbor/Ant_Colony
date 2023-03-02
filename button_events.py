class ButtonEvents:
    """Class for storage logic of button events"""

    def __init__(self, ac_prog):
        self.ac_prog = ac_prog
        self.prog_stat = self.ac_prog.prog_stat

    def click_start_button(self):
        """Start program if no started"""
        if self.prog_stat.initial_state.is_active:
            self.prog_stat.start_program()
