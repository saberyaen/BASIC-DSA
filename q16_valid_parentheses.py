def is_valid_parentheses(s: str) -> bool:
    """Check whether brackets are balanced and correctly nested."""
    matching = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
    return not stack


if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    print(is_valid_parentheses(s))
