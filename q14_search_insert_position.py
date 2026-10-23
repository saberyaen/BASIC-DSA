def search_insert_position(arr: list[int], target: int) -> int:
    """Return target index if found, otherwise its insertion index."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted elements: ").split()))
    target = int(input("Enter target: "))
    print(search_insert_position(arr, target))
