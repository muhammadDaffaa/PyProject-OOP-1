import time

class MadLib:
    def __init__(self):
        pass

    def get_input(self: str):
        user_input: str = input(f"Enter a {self}")
        return user_input


# Input String
input1 = MadLib.get_input("Your Input-1 : ")
input2 = MadLib.get_input("Your Input-2 : ")

start_second = time.time()
result = f"""
These are your
Input 1 is {input1}
Input 1 is {input2}
"""
end_second = time.time()

print(result)

result_second = start_second - end_second

print(f"{result_second} seconds")
