def sum_of_digits(n: int) -> int:
    """Return the sum of the decimal digits of an integer."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print(sum_of_digits(n))
