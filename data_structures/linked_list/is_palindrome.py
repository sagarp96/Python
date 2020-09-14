def is_palindrome(head):
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None  # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


def is_palindrome_stack(head):
    if not head or not head.next:
        return True

    # 1. First transverse the list and append  each element into the stack
    p1=head
    stack=[]
    while p1:
        app=stack.append(p1.val)
        p1=p1.next

    # 2. again transverse the list and compare the list while popping through the stack, if element is not equal then its not a palindrom
    while head:
        i=stack.pop()
        if head.data==i:
            return True
        else:
            return False
            break
        head=head.next
    return True

def is_palindrome_dict(head):
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d.keys():
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
