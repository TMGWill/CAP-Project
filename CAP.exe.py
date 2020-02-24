from CAP_Personality_Class import CAP_P
from CAP_Art_Class import CAP_A
import time


def main():
    """
    The program executes the conversation which
    will use the values produced to create an
    abstract drawing using turtles.

    :return: None
    """

    cap_p = CAP_P()

    cap_p.start_convo()
    cap_p.dogs_and_cats()
    start = cap_p.start_pos()
    loop = cap_p.ask_age()
    multiplier = cap_p.age_num_multiplier()
    side_a = cap_p.fake_guessing_game_low()
    side_b = cap_p.fake_guessing_game_high()
    length = cap_p.ask_height()
    color = cap_p.ask_fav_color()
    cap_p.end_convo()

    time.sleep(3)

    cap_a = CAP_A(start, loop * multiplier, side_a, side_b, length, color)
    cap_a.create_art()


main()
