from sources.mad_lib import MadLib
from sources.dice_simulator import DiceSimulator
from sources.number_guess_game import NumberGuess
from sources.hangman import Hangman
from sources.rock_paper_cutter import Hompimpa


# Call Class
def my_madlib():
    input1 = MadLib()

    input1.set_input("Your First number : ")
    print(input1.get_result())


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


def my_hangman():
    test1 = Hangman()

    test1.get_REQ()
    test1.run_game()


def my_rpc():
    pass


if __name__ == "__main__":
    #! Change the name of function. If you want to run it
    # my_madlib()  # 1
    # my_number_guess_game()  # 2
    # my_dice_simulator()  # 3
    my_hangman()  # 4
