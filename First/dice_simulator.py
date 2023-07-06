import random

class DiceSimulator:

    # Constructor
    def __init__(self):
        self.__temp_list = []
        self.__user_input = ''

    def set_roll_dice(self, amount):
        if amount <= 0:
            raise ValueError
        self.__temp_list = []
        for i in range(amount):
            random_roll: int = random.randint(1, 6)
            self.__temp_list.append(random_roll)

        return self.__temp_list

    def get_roll_dice(self) -> 'list[int]':
        return print(self.__temp_list)

    def set_process_roll_dice(self):
        while True:
            try:
                self.__user_input: str = input('How many dice would you like to troll ?')

                if self.__user_input == 'exit':
                    print('Thanks for playing')
                    break

                self.set_roll_dice(int(self.__user_input))
                self.get_roll_dice()

            except ValueError:
                print("Please enter the true number of dice")
