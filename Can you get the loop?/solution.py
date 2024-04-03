def loop_size(node):
    cur = node
    fast_next = node.next
    i = 0
    met = False
    while node:
        if cur is fast_next:
            if not met:
                met = True
                i = 0
            else:
                return i
        cur = cur.next
        fast_next = fast_next.next.next
        i += 1