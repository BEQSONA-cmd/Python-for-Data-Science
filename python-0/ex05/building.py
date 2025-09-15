import sys


def error_handle():
    """
    this function handles errors from wrong arguments
    and returns text
    """

    text = ""
    if len(sys.argv) == 1:
        text = sys.stdin.read()
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if not text:
        raise AssertionError("No text provided")
    return text


def main():
    """
    this is main function
    """

    text = error_handle()

    upper = 0
    lower = 0
    number = 0
    space = 0
    punctuation_marks = 0

    for character in text:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
        elif character.isdigit():
            number += 1
        elif character.isspace():
            space += 1
        else:
            punctuation_marks += 1

    sum = upper + lower + number + space + punctuation_marks

    print(f"The text contains {sum} characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation_marks, "punctuation marks")
    print(space, "spaces")
    print(number, "digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(error)
