#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        lr = p = None
        carry = False
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            r = a + b
            if carry:
                r += 1

            carry = bool(r / 10)
            node = ListNode(r % 10)
            # Record result list head
            if not lr:
                lr = node

            if p:
                p.next = node

            p = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return lr


def print_list(list_head):
    print_l(list_head)
    print '\n'


def print_l(list_head):
    if list_head:
        print list_head.val,
        print_l(list_head.next)


if __name__ == '__main__':
    l1a = ListNode(5)
    l1 = l1a

    l2a = ListNode(5)
    l2 = l2a

    s = Solution()
    lr = s.addTwoNumbers(l1, l2)
    print_list(l1)
    print_list(l2)
    print_list(lr)
