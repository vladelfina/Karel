from stanfordkarel import *

def main():
    start_line()
    middle_of_line()
    end_this_story()

def end_this_story():
    turn_180_degree()
    if no_beepers_present():
        move()
        turn_180_degree()
    if no_beepers_present():
        put_beeper()

def middle_of_line():
    turn_180_degree()
    pick_beeper()
    go_if_can()
    while beepers_present():
        move()
    if no_beepers_present():
        turn_180_degree()
        move()
        pick_beeper()
    go_if_can()
    step_forward()
    if beepers_present():
        pick_beeper()
        turn_180_degree()
        move()

def start_line():
    put_beeper()
    go_ahead()
    put_beeper()
    turn_180_degree()
    go_ahead()
    find_next_beeper()
    find_next_beeper()
    turn_180_degree()
    if no_beepers_present():
        move()
        move()
    while no_beepers_present():
        put_beeper()
        move()

def find_next_beeper():
    turn_180_degree()
    step_forward()
    find_beeper()
    go_ahead()

def go_if_can():
    # If front clear Karel make 1 step
    if front_is_clear():
        move()

def step_forward():
    # If beepeer here, move Karel
    if beepers_present():
        move()

def go_ahead():
    # Karel go when front is clear
    while front_is_clear():
        move()

def find_beeper():
    # Karel try to find beepers
    if no_beepers_present():
        turn_180_degree()
        move()
        turn_180_degree()
        pick_beeper()
        move()
        put_beeper()

def turn_180_degree():
    # Karel turn around
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("StoneMasonKarel.w")