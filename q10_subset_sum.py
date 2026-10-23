def subset_sum_exists(arr: list[int], target: int) -> bool:
    """Return True if any subset of arr sums to target."""
    def search(index: int, remaining: int) -> bool:
        if remaining == 0:
            return True
        if index == len(arr):
            return False
        return search(index + 1, remaining - arr[index]) or search(index + 1, remaining)

    return search(0, target)


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
    target = int(input("Enter target sum: "))
    print(subset_sum_exists(arr, target))
