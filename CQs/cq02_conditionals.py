__author__ = "730754025"


def guess_a_number() -> None:
    """Guesses a secret number"""
    secret: int = 7
    response = int(input("Guess a number:"))
    print("Your guess was " + str(response))
    if response == secret:
        print("You got it!")
    elif response < secret:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
