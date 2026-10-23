class MinStack:
    """Stack supporting push, pop, top, and minimum in O(1) time."""
    def __init__(self) -> None:
        self._stack: list[int] = []
        self._mins: list[int] = []

    def push(self, value: int) -> None:
        self._stack.append(value)
        if not self._mins or value <= self._mins[-1]:
            self._mins.append(value)

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        value = self._stack.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def top(self) -> int:
        if not self._stack:
            raise IndexError("top from empty stack")
        return self._stack[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("minimum from empty stack")
        return self._mins[-1]


if __name__ == "__main__":
    stack = MinStack()
    for value in [3, 5, 2, 1, 1]:
        stack.push(value)
    print("Minimum:", stack.get_min())
    stack.pop()
    print("Minimum after pop:", stack.get_min())
