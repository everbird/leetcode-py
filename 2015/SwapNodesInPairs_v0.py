class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def print_l(head):
    if head:
        print head.val

        if head.next:
            print_l(head.next)


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        r = p = ListNode(0)
        while head and head.next:
            b = head.next
            c = b.next if b else None
            p.next = b
            p = head

            b.next = head
            head.next = c
            head = c

        p.next = head
        return r.next


if __name__ == '__main__':
    head = n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    r = s.swapPairs(head)
    print_l(r)
