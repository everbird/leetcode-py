#!/usr/bin/env python3
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(head)


def merge_sort(head):
    hlen = llen(head)

    def _merge_sort(node, length):
        if length == 0:
            return
        elif length == 1:
            node.next = None
            return node

        m = length // 2

        pre = None
        h1 = h2 = node
        for i in range(m):
            pre = h2
            h2 = h2.next

        pre.next = None
        h1 = _merge_sort(h1, m)
        h2 = _merge_sort(h2, length - m)

        return _merge(h1, h2)

    def _merge(h1, h2):
        dummy = p = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                _next = h1.next
                p.next = h1
                p = p.next
                h1.next = None
                h1 = _next
            else:
                _next = h2.next
                p.next = h2
                p = p.next
                h2.next = None
                h2 = _next

        if h1:
            p.next = h1

        if h2:
            p.next = h2

        return dummy.next

    return _merge_sort(head, hlen)



def llen(head):
    if not head:
        return 0

    r = 0
    while head:
        r += 1
        head = head.next

    return r


if __name__ == '__main__':
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    s.sortList(n1)
