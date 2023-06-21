from random import randint


class NumberGuess:

    def __init__(self):
        self.__enter_lower_num = 0
        self.__enter_higher_num = 0
        self.__user_number_guess: int = 0
        self.__number_guess: int = 0
        self.__random_number: int = 0
        pass

    def set_lower_num(self):
        self.__enter_lower_num: int = int(input(f"Enter your LOWER number : "))

    def get_lower_num(self):
        return self.__enter_lower_num

    def set_higher_number(self):
        self.__enter_higher_num: int = int(input(f"Enter your HIGHER number : "))

    def get_higher_number(self):
        return self.__enter_higher_num

    def set_random_number(self):
        self.__random_number = randint(self.__enter_lower_num, self.__enter_higher_num)

    def get_random_number(self):
        return self.__random_number

    def number_time_guess(self):
        return self.__number_guess

    # def get_print(self):
    #     print(f"Guess the number in the range from {self.__enter_lower_num} to {self.__enter_higher_num}")

# while True :
#     try:
#         user_guess:int = int(input(f"Input your number : "))
#     except ValueError as e:
#         print("Please correct the input")
#         continue
#
#     number_guess+=1
#
#     if user_guess > random_number:
#         print("Your guess is bigger")
#     elif user_guess < random_number:
#         print("Your guess is lower")
#     else:
#         print("Congrats, Your guess is correct !!")
#         break
#
#     print(f"You have guess in {number_guess} times !!! ")
