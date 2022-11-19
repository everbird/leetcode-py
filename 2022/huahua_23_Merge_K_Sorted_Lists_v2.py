#!/usr/bin/env python3

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lenn = len(lists)
        if lenn == 0:
            return
        elif lenn == 1:
            return lists[0]

        m = lenn // 2
        r1 = self.mergeKLists(lists[:m])
        r2 = self.mergeKLists(lists[m:])
        return merge_sort(r1, r2)



def merge_sort(h1, h2):
    dummy = p = ListNode(None)
    while h1 and h2:
        if h1.val < h2.val:
            p.next = h1
            _next = h1.next
            p = p.next
            h1.next = None
            h1 = _next
        else:
            p.next = h2
            _next = h2.next
            p = p.next
            h2.next = None
            h2 = _next

    if h1:
        p.next = h1
    elif h2:
        p.next = h2

    return dummy.next
