def get_input(getInput: str):
    user_input: str = input(f"Enter a {getInput}")
    return user_input


# Input String
input1 = get_input("Your Input-1 : ")
input2 = get_input("Your Input-2 : ")

result = f"""
These are your
Input 1 is {input1}
Input 2 is {input2}
"""

print(result)
