#!/usr/bin/env python3

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carrier = 0
        r = p = ListNode(None)

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            _sum = v1 + v2 + carrier
            v = _sum % 10
            carrier = _sum // 10

            p.next = ListNode(v)
            p = p.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carrier:
            p.next = ListNode(carrier)

        return r.next
