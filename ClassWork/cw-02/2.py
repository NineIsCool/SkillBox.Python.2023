def fibonacci(n: int) -> int:
    """
    Функция nth_fibonacci находит n-ое число Фибоначчи.

    Parameters:
        a (int): Порядковый номер числа.

    Returns:
        int: n-ое число Фибоначчи.

    Examples:
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(8)
        21
        >>> fibonacci(0)
        0
        >>> fibonacci("sd")
        'Invalid input'
        >>> fibonacci(-12)
        'Invalid input'
        >>> fibonacci(5.234)
        'Invalid input'

    """
    if not isinstance(n, int):
        return "Invalid input"
    if n < 0 or n % 1 != 0:
        return "Invalid input"

    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    import cProfile

    cProfile.run('fibonacci(10)')