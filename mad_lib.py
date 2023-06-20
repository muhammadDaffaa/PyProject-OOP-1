import time

class MadLib:
    def __init__(self):
        pass

    def get_input(self: str,new_input):
        user_input: str = input(f"Enter a {new_input}")
        self.input1 = user_input
        # return user_input

    def get_print(self:str):
        result = f"""
        These are your
        Input 1 is {self.input1}
        """
        return result

    def start_second(self):
        pass
        # return self.time()