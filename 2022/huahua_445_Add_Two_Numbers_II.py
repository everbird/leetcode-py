#!/usr/bin/env python3

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        llen1 = llen(l1)
        llen2 = llen(l2)
        if llen1 > llen2:
            l1, l2 = l2, l1
            llen1, llen2 = llen2, llen1

        h1, h2 = l1, l2

        dummy = p = ListNode(None)
        s = []
        for i in range(llen2):
            if i + llen1 < llen2:
                s.append((l2, ListNode(0)))
                l2 = l2.next
            else:
                s.append((l2, l1))
                l1 = l1.next
                l2 = l2.next

        carrier = 0
        nh = n = ListNode(None)
        while s:
            l1, l2 = s.pop()
            _sum = l1.val + l2.val + carrier
            v = _sum % 10
            carrier = _sum // 10
            n.next = ListNode(v)
            n = n.next

        if carrier:
            n.next = ListNode(carrier)
            n = n.next

        p.next = reverse(nh.next)
        return dummy.next


def llen(node):
    if not node:
        return 0

    r = 0
    while node:
        r += 1
        node = node.next

    return r

def reverse(node):
    pre = None
    while node:
        _next = node.next
        node.next = pre
        pre = node
        node = _next

    return pre
