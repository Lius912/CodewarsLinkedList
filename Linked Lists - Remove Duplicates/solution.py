class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    node = head
    equal_node = None
    while node is not None:
        if not equal_node and node.next is not None and node.data == node.next.data:
            equal_node = node
        elif equal_node and (node.next is None or equal_node.data != node.next.data):
            equal_node.next = node.next
            equal_node = None
        node = node.next
    return head