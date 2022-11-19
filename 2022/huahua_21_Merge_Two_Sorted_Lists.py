#!/usr/bin/env python3

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(list1, list2)

def merge_sort(h1, h2):
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
    elif h2:
        p.next = h2

    return dummy.next
