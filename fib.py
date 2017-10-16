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
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
