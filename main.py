# Import Class from different file
from mad_lib import MadLib
from number_guess_game import NumberGuess
from dice_simulator import DiceSimulator


# Call Class
def my_madlib():
    input1 = MadLib()
    input2 = MadLib()

    input1.set_input("Your First number : ")
    input2.set_input("Your Second number : ")
    input1.get_print()
    input2.get_print()


def my_number_guess_game():
    test1 = NumberGuess()

    test1.set_lower_num()
    test1.set_higher_number()
    test1.set_random_number()
    test1.get_random_number()
    test1.get_print()


def my_dice_simulator():
    test1 = DiceSimulator()

    test1.set_process_roll_dice()


if __name__ == '__main__':
    # Change the name of function. If you want to run it
    # my_madlib()  # 1
    # my_number_guess_game()  # 2
    my_dice_simulator()  # 3
