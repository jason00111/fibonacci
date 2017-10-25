def fib(n, i=0, a=0, b=1):
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
    if i < n:
        return fib(n, i+1, b, a+b)
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
