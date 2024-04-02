class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def stringify(node):
    outputs = []
    while node is not None:
        outputs.append(str(node.data))
        node = node.next
    return " -> ".join(outputs + ["None"])