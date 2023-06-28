class MadLib:
    # Constructor
    def __init__(self):
        self.__data_input = '' #Private attribute

    def set_input(self: str,new_input):
        user_input: str = input(f"Enter a {new_input}")
        self.__data_input = user_input
        # return user_input

    def get_print(self:str):
        result = f"""
        This is your
        Input {self.__data_input}
        """
        print(result)
        # return result
