#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        return "<{}({}):{}:{}>".format(self.label, id(self), id(self.next), id(self.random))


def printl(n):
    print n
    if n.next:
        printl(n.next)


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        d = {}
        h = head
        nh = None
        while h:
            n = RandomListNode(h.label)
            if not nh:
                nh = n

            d[h] = n
            h = h.next

        h = head
        while h:
            if h.next:
                d[h].next = d[h.next]
            if h.random:
                d[h].random = d[h.random]
            h = h.next

        return nh


if __name__ == '__main__':
    s = Solution()

    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n1.random = n4
    n2.random = n2
    n3.random = n2
    n4.random = None

    new_head = s.copyRandomList(head)

    printl(head)
    print '-' * 6
    printl(new_head)
