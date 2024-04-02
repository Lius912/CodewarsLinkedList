class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return head
    def reverse_recursion(head):
        if head.next is None:
            return Node(head.data), None
        new_head, node = reverse_recursion(head.next)
        if node is None:
            new_head.next = Node(head.data)
            return new_head, new_head.next
        node.next = Node(head.data)
        return new_head, node.next
    return reverse_recursion(head)[0]