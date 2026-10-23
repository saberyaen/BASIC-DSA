def next_greater_elements(arr: list[int]) -> list[int]:
    """For each element, return the next greater value to its right, or -1."""
    result = [-1] * len(arr)
    stack: list[int] = []  # Indices whose next greater value is not found yet

    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] < value:
            result[stack.pop()] = value
        stack.append(i)
    return result


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(next_greater_elements(arr))
