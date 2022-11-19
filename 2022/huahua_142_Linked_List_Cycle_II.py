#!/usr/bin/env python3

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 or p2:
            p1 = p1.next
            for i in range(2):
                if p2:
                    p2 = p2.next

            if p1 == p2:
                break

        if p1 is None and p2 is None:
            return

        p = head
        while p != p1:
            p = p.next
            p1 = p1.next

        return p
