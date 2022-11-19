#!/usr/bin/env python3

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        if not head.next:
            return head

        p1 = head
        p2 = head.next

        dummy = pre = ListNode(None)
        while p1 and p2:
            pre.next = p2
            p1.next = None
            _next = p2.next
            p2.next = p1
            pre = p1
            p1 = _next
            p2 = _next.next if _next else None

        if p1 and not p2 and pre:
            pre.next = p1

        return dummy.next
