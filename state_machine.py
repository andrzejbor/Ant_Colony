from statemachine import StateMachine, State


class ProgramState(StateMachine):
    """Class to managing program state"""
    # Program states
    ant_move_state = State("ant_move", initial=True)
    show_results_state = State("show_results")

    # Transitions of the state
    switch_to_show_result = ant_move_state.to(show_results_state)
    switch_to_ant_move = show_results_state.to(ant_move_state)
