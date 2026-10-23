def insert_at_bottom(stack: list[int], value: int) -> None:
    if not stack:
        stack.append(value)
        return
    top = stack.pop()
    insert_at_bottom(stack, value)
    stack.append(top)


def reverse_stack(stack: list[int]) -> None:
    """Reverse stack in place using recursion and no extra stack."""
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)


if __name__ == "__main__":
    stack = list(map(int, input("Enter stack values from bottom to top: ").split()))
    reverse_stack(stack)
    print("Reversed stack (bottom to top):", stack)
