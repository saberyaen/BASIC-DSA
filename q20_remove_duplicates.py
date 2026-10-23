class Node:
    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


def remove_duplicates(head: Node | None) -> Node | None:
    """Remove duplicates from a sorted singly linked list in place."""
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head: Node | None) -> None:
    values = []
    while head:
        values.append(str(head.value))
        head = head.next
    print(" -> ".join(values) if values else "(empty)")


if __name__ == "__main__":
    values = list(map(int, input("Enter sorted list values: ").split()))
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    print("Before:")
    print_list(head)
    head = remove_duplicates(head)
    print("After:")
    print_list(head)
