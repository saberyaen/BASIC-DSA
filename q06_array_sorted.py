def is_sorted(arr: list[int], index: int = 0) -> bool:
    """Check whether arr is in non-decreasing order using recursion."""
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
    print(is_sorted(arr))
