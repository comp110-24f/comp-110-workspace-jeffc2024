"""Practicing my conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=7)

print(less_than_10(num=2))
