#!/usr/bin/env python3

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = reverse(l1)
        l2 = reverse(l2)
        h = add(l1, l2)
        return reverse(h)

def add(l1, l2):
    carrier = 0
    dummy = p = ListNode(None)
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
        p = p.next

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
