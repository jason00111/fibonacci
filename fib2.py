def fib(n):
    """Return the nth fibonacci number.

    >>> fib(6)
    8
    >>> [fib(n) for n in range(6)]
    [0, 1, 1, 2, 3, 5]
    >>> fib(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")

    i, a, b = 0, 0, 1

    while i < n:
        a, b = b, a+b
        i += 1
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
