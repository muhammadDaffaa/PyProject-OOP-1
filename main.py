# Import Class from different file
from mad_lib import MadLib
from number_guess_game import NumberGuess

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



if __name__ == '__main__':
    # Change the name of function that you want to run
    # my_madlib()  # 1
    my_number_guess_game() #2
