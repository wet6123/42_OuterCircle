import sys


NESTED_MORSE = {
    " ": "/ ",
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
    "9": "----. "
}


def encode_to_morse(text):
    """
    모스코드로 문자열을 인코딩하는 함수.
    """
    morse_code = ""
    for char in text.upper():
        morse_code += NESTED_MORSE[char]

    return morse_code.rstrip()


def validate_arguments():
    """
    인수를 검증하는 함수.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    text = sys.argv[1]

    for char in text:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")

    return text


def main():
    """
    메인 함수
    """
    try:
        text = validate_arguments()
        morse_result = encode_to_morse(text)
        print(morse_result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
