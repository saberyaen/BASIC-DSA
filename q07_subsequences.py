def subsequences(s: str) -> list[str]:
    """Return every subsequence of s, including the empty string."""
    result: list[str] = []

    def build(index: int, current: str) -> None:
        if index == len(s):
            result.append(current)
            return
        build(index + 1, current)          # Exclude current character
        build(index + 1, current + s[index])  # Include current character

    build(0, "")
    return result


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(*subsequences(s), sep="\n")
