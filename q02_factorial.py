def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print(factorial(n))
