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
        if not head:
            return

        if not head.next:
            return head

        new_head = head.next
        pre = None
        while head:
            a = head
            b = head.next
            if not b:
                break
            head = b.next
            # swap
            a.next = head
            b.next = a
            if pre:
                pre.next = b
            pre = a

        return new_head


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
