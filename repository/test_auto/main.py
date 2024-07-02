def factorials(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif isinstance(n, int):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    else:
        raise TypeError("Only integer values are allowed.")
