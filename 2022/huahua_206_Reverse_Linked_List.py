#!/usr/bin/env python3

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverse(head)

def reverse(node):
    if not node:
        return

    pre = None
    while node:
        _next = node.next
        node.next = pre
        pre = node
        node = _next

    return pre
