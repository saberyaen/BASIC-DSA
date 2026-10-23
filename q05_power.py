def power(x: float, n: int) -> float:
    """Compute x**n recursively, including negative integer exponents."""
    if n == 0:
        return 1
    if n < 0:
        if x == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        return 1 / power(x, -n)
    half = power(x, n // 2)
    result = half * half
    return result if n % 2 == 0 else x * result


if __name__ == "__main__":
    x = float(input("Enter x: "))
    n = int(input("Enter integer exponent n: "))
    print(power(x, n))
