import time

class MadLib:
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2

    def get_input(self: str,new_input):
        user_input: str = input(f"Enter a {new_input}")
        # return user_input

    def __str__(self:str):
        result = f"""
        These are your
        Input 1 is {self.input1}
        Input 2 is {self.input2}
        """
        return result

    def start_second(self):
        pass
        # return self.time()