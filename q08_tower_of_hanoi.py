def tower_of_hanoi(n: int, source: str, auxiliary: str, destination: str) -> None:
    """Print the moves needed to transfer n disks."""
    if n <= 0:
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    tower_of_hanoi(n, "A", "B", "C")
