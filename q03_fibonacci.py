def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, with F(0)=0 and F(1)=1."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Enter index N: "))
    print(fibonacci(n))
