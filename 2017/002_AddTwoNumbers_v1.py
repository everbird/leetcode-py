#!/usr/bin/env python
# encoding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        head = p = None
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            r = l1_val + l2_val + carry
            if r >= 10:
                carry = r // 10
                r = r % 10
            else:
                carry = 0

            if not p:
                head = p = ListNode(r)
            else:
                p.next = ListNode(r)
                p = p.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            p.next = ListNode(1)

        return head


def print_list(list_head):
    print_l(list_head)
    print '\n'


def print_l(list_head):
    if list_head:
        print list_head.val,
        print_l(list_head.next)


if __name__ == '__main__':
    l1a = ListNode(2)
    l1b = ListNode(4)
    l1c = ListNode(3)
    l1a.next = l1b
    l1b.next = l1c
    l1 = l1a

    l2a = ListNode(5)
    l2b = ListNode(6)
    l2c = ListNode(4)
    l2a.next = l2b
    l2b.next = l2c
    l2 = l2a

    s = Solution()
    lr = s.addTwoNumbers(l1, l2)
    print_list(l1)
    print_list(l2)
    print_list(lr)

    print '>>>>>>'
    l1a = ListNode(5)
    l1 = l1a

    l2a = ListNode(5)
    l2 = l2a

    s = Solution()
    lr = s.addTwoNumbers(l1, l2)
    print_list(l1)
    print_list(l2)
    print_list(lr)
