def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]


def main():
    """메인 함수"""
    pass


if __name__ == "__main__":
    main()
