def print_1_to_n(n: int) -> None:
    """Print numbers from 1 to n using recursion."""
    if n <= 0:
        return
    print_1_to_n(n - 1)
    print(n)


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print_1_to_n(n)
