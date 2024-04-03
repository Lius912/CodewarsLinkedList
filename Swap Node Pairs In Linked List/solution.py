class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head:
        return head
    node = head
    if head and head.next:
        head = head.next
    first_in_last_pair = None
    while node and node.next:
        tail = node.next.next
        swapped_node = node.next
        node.next = tail
        swapped_node.next = node
        if first_in_last_pair:
            first_in_last_pair.next = swapped_node
        first_in_last_pair = node
        node = node.next
    return head
        