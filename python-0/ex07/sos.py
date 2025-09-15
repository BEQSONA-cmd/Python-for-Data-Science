import sys


def get_morse_code():
    """
    returns nested morse code as an dictionary
    """
    NESTED_MORSE = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        " ": "/ "
    }
    return NESTED_MORSE


def sos():
    """
    converts string to morse code
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    arg_str = sys.argv[1].upper()
    NESTED_MORSE = get_morse_code()
    morse_str = ""
    for char in arg_str:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_str += NESTED_MORSE[char]

    print(morse_str)


if __name__ == "__main__":
    try:
        sos()
    except AssertionError as error:
        print("AssertionError:", error)
