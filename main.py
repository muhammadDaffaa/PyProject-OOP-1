#Import Class from different file
from mad_lib import MadLib
from number_guess_game import NumberGuess

# Call Class
def myMadLib():
    input1 = MadLib()
    input2 = MadLib()

    input1.get_input("Your First number : ")
    input2.get_input("Your Second number : ")
    input1.get_print()
    input2.get_print()

if __name__ == '__main__':
    # Change the name of function that you want to run
    myMadLib()
