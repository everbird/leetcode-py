#!/usr/bin/env python3

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return has_cycle(head)

def has_cycle(node):
    if not node or not node.next:
        return False

    p1 = p2 = node
    while p1 and p2:
        p1 = p1.next
        p2 = p2.next
        if p2:
            p2 = p2.next

        if p1 == p2:
            return True

    return False
