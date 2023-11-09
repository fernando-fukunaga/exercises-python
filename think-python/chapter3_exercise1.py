"""
Write a function called right_justify that takes a string s as a parameter and prints
the string in a way that the last char is on the column 70 of the screen
"""

def right_justify(s: str):
    remaining_spaces = 70 - len(s)
    new_string = remaining_spaces * " " + s
    print(new_string)

right_justify("python")