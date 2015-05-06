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
        if not lists:
            return None

        lenl = len(lists)
        if lenl == 1:
            return lists[0]

        return merge_two_lists(
            self.mergeKLists(lists[:lenl // 2]),
            self.mergeKLists(lists[lenl // 2:])
        )


def merge_two_lists(l1, l2):
    head = p = ListNode(0)
    if not l1:
        return l2

    if not l2:
        return l1

    while l1 and l2:
        if l1.val < l2.val:
            p.next = ListNode(l1.val)
            l1 = l1.next
        else:
            p.next = ListNode(l2.val)
            l2 = l2.next

        p = p.next

    if not l1:
        p.next = l2
    elif not l2:
        p.next = l1

    return head.next


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
    #r = merge_two_lists(m1, o1)
    print_l(r)
