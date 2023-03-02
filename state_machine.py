from statemachine import StateMachine, State


class ProgramState(StateMachine):
    """Class to managing program state"""
    # Program states
    initial_state = State("initial", initial=True)
    ant_move_state = State("ant_move")
    show_results_state = State("show_results")
    pause_state = State("pause")
    end_program_state = State("end_prog")

    # Transitions of the state
    # Run transitions
    switch_to_show_result = ant_move_state.to(show_results_state)
    switch_to_ant_move = show_results_state.to(ant_move_state)
    # Start and restart transitions
    start_program = initial_state.to(ant_move_state)
    restart_program = pause_state.to(ant_move_state)
    # Pause transitions
    from_ant_to_pause = ant_move_state.to(pause_state)
    from_show_to_pause = show_results_state.to(pause_state)
    # End program transitions
    switch_to_end = show_results_state.to(end_program_state)
