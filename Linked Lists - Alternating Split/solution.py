class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError()
    even_head = Node(head.data)
    cur_even = even_head
    odd_head = Node(head.next.data)
    cur_odd = odd_head
    i = 0
    head = head.next.next
    while head:
        if i & 1:
            cur_odd.next = Node(head.data)
            cur_odd = cur_odd.next
        else:
            cur_even.next = Node(head.data)
            cur_even = cur_even.next
        head = head.next
        i += 1
    return Context(even_head, odd_head)
            