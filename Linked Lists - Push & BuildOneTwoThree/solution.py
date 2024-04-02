class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    temp = head
    head = Node(data)
    head.next = temp
    return head

def build_one_two_three():
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    return node