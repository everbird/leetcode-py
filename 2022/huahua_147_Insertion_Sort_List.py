#!/usr/bin/env python3

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = p = ListNode(None)
        while head:
            pre = dummy
            p = dummy.next
            while p:
                if p.val >= head.val:
                    break

                pre = p
                p = p.next

            hnext = head.next
            head.next = p
            pre.next = head

            head = hnext

        return dummy.next
