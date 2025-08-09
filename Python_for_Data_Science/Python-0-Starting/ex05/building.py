import sys


def count_characters(text):
    """문자열의 각 문자 유형별 개수를 세는 함수"""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in punctuation:
            punct_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    return upper_count, lower_count, punct_count, space_count, digit_count


def main():
    """인수를 처리하고 문자 개수를 출력하는 함수"""
    if len(sys.argv) == 1:
        text = input("Please enter a text:\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return

    upper, lower, punct, space, digit = count_characters(text)
    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    main()
