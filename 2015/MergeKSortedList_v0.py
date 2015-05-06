#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_l(head):
    if head:
        print head.val

        if head.next:
            print_l(head.next)

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        head = p = ListNode(0)
        while any(lists):
            n = yield_node(lists)
            p.next = n
            p = n

        return head.next


def yield_node(lists):
    r = 0
    min_v = 2**31
    for i, li in enumerate(lists):
        if li and min_v > li.val:
            min_v = li.val
            r = i

    p = lists[r]
    lists[r] = p.next
    return ListNode(p.val)


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(5)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(2)
    m2 = ListNode(6)
    m3 = ListNode(7)
    m1.next = m2
    m2.next = m3

    o1 = ListNode(2)
    o2 = ListNode(4)
    o3 = ListNode(9)
    o1.next = o2
    o2.next = o3

    s = Solution()
    r = s.mergeKLists([n1, m1, o1])
    print_l(r)
