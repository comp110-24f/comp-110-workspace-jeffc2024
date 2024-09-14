"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730754025"


def input_word() -> str:
    user_word = input("Enter a 5-character word:")
    if len(user_word) == 5:
        return user_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    user_letter = input("Enter a single character:")
    if len(user_letter) == 1:
        return user_letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """main part of comparing letters to words, use loops normally"""
    count = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        """final else statement where instances found"""
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """main function, set variables and return types equal here"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
