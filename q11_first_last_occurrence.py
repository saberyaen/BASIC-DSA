def first_occurrence(arr: list[int], target: int) -> int:
    """Return first index of target in sorted arr, or -1."""
    left, right, answer = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            if arr[mid] == target:
                answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


def last_occurrence(arr: list[int], target: int) -> int:
    """Return last index of target in sorted arr, or -1."""
    left, right, answer = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            if arr[mid] == target:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted elements: ").split()))
    target = int(input("Enter target: "))
    print("First:", first_occurrence(arr, target))
    print("Last:", last_occurrence(arr, target))
