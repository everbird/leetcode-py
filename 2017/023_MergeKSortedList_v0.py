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
        len_l = len(lists)
        if len_l == 0:
            return

        if len_l == 1:
            return lists[0]

        if len_l == 2:
            return mergeTwoLists(lists[0], lists[1])

        return mergeTwoLists(
            self.mergeKLists(lists[:len_l // 2]),
            self.mergeKLists(lists[len_l // 2:]),
        )


def mergeTwoLists(a, b):
    if not a:
        return b

    if not b:
        return a

    p = head = None
    while a or b:
        is_a_selected = b is None or (a is not None and a.val < b.val)
        smaller = a if is_a_selected else b
        if not head:
            head = smaller

        if p:
            p.next = smaller

        p = smaller
        if is_a_selected:
            a = a.next
        else:
            b = b.next

    return head


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
