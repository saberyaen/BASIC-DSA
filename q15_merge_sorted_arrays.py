def merge_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    i = j = 0
    merged: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


if __name__ == "__main__":
    a = list(map(int, input("Enter first sorted array: ").split()))
    b = list(map(int, input("Enter second sorted array: ").split()))
    print(merge_sorted_arrays(a, b))
