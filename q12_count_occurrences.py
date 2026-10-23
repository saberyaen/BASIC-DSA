try:
    from .q11_first_last_occurrence import first_occurrence, last_occurrence
except ImportError:  # Allows running this file directly from the searching directory
    from q11_first_last_occurrence import first_occurrence, last_occurrence


def count_occurrences(arr: list[int], target: int) -> int:
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    return last_occurrence(arr, target) - first + 1


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted elements: ").split()))
    target = int(input("Enter target: "))
    print(count_occurrences(arr, target))
