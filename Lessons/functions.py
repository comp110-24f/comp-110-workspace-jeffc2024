from random import randint

"""Practices with a functione"""


# Define a function
def sum(num1: int, num2: int) -> int:  # function signature
    """Return num1+num2"""
    return num1 + num2


# Call the function
sum(num1=1, num2=10)  # <-1 and 10 are arguments
sum(num1=randint(1, 10), num2=randint(2, 20))
