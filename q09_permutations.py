def permutations(s: str) -> list[str]:
    """Return all permutations of s. Duplicate letters may create duplicates."""
    result: list[str] = []

    def backtrack(chars: list[str], start: int) -> None:
        if start == len(chars):
            result.append("".join(chars))
            return
        for i in range(start, len(chars)):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(chars, start + 1)
            chars[start], chars[i] = chars[i], chars[start]  # Undo swap

    backtrack(list(s), 0)
    return result


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(*permutations(s), sep="\n")
