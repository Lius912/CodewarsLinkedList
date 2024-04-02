class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    lst = s.split(" -> ")[:-1]
    return list_to_linked_list(lst)

def list_to_linked_list(lst):
    if not lst:
        return None
    if not lst[1:]:
        return Node(int(lst[0]))
    return Node(int(lst[0]), list_to_linked_list(lst[1:]))