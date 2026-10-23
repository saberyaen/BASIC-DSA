def floor_ceil(arr: list[int], target: int) -> tuple[int | None, int | None]:
    """Return (floor, ceil) values in a sorted array; None if absent."""
    floor_value = None
    ceil_value = None
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid], arr[mid]
        if arr[mid] < target:
            floor_value = arr[mid]
            left = mid + 1
        else:
            ceil_value = arr[mid]
            right = mid - 1
    return floor_value, ceil_value


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted elements: ").split()))
    target = int(input("Enter target: "))
    print("Floor, ceil:", floor_ceil(arr, target))
