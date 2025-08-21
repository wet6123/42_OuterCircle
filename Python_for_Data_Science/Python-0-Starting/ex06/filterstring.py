import sys


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]


def validate_arguments():
    """
    Validate command line arguments.

    Returns:
        tuple: (string, integer) if validation successful

    Raises:
        AssertionError: If arguments are invalid
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    string_arg = sys.argv[1]
    number_arg = sys.argv[2]

    if not isinstance(string_arg, str):
        raise AssertionError("the arguments are bad")

    try:
        N = int(number_arg)
    except ValueError:
        raise AssertionError("the arguments are bad")

    return string_arg, N


def filter_words_by_length(text, min_length):
    """
    Filter words from text that have length greater than min_length.

    Args:
        text (str): Input string containing words separated by spaces
        min_length (int): Minimum length threshold

    Returns:
        list: List of words with length > min_length
    """
    words = text.split()

    filtered_words = ft_filter((lambda word: len(word) > min_length), words)

    return filtered_words


def main():
    """
    Main function that processes command line arguments and filters words.
    """
    try:
        string_arg, N = validate_arguments()

        result = filter_words_by_length(string_arg, N)

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
