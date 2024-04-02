class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    node = head
    if node is None:
        return Node(data)
    if node.data > data:
        head = Node(data)
        head.next = node
        return head
    while node.next is not None:
        if node.next.data > data:
            tail = node.next
            node.next = Node(data)
            node.next.next = tail
            break
        node = node.next
    if node.next is None:
        node.next = Node(data)
    return head