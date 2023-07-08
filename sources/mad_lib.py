class MadLib:
    # Constructor
    def __init__(self):
        self.__data_input = '' #Private attribute
        self.__user_input = '' #Private attribute

    def set_input(self,new_input):
        self.__user_input: str = input(f"Enter a {new_input}")
        self.__data_input = self.__user_input
        

    def get_result(self:str):
        result = f"""
        This is your
        Input {self.__data_input}
        """
        return result
