def reverseList(head):
    """Reverse a singly linked list in place and return its new head."""
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev