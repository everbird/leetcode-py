#!/usr/bin/env python3

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = p = ListNode(None)

        while any(lists):
            minh = None
            mini = -1
            for i, h in enumerate(lists):
                if not h:
                    continue

                if not minh or h.val < minh.val:
                    minh = h
                    mini = i

            _next = minh.next

            p.next = minh
            p = p.next

            minh.next = None

            lists[mini] = _next

        return dummy.next
