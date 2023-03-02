from statemachine import StateMachine, State


class ProgramState(StateMachine):
    """Class to managing program state"""
    # Program states
    initial_state = State("initial", initial=True)
    ant_move_state = State("ant_move")
    show_results_state = State("show_results")

    # Transitions of the state
    switch_to_show_result = ant_move_state.to(show_results_state)
    switch_to_ant_move = show_results_state.to(ant_move_state)
    start_program = initial_state.to(ant_move_state)
