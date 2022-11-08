#!/usr/bin/env python3

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        rs_left = []
        rs_right = []
        q = [(root, 0, 0)]
        while q:
            n, x, y = q.pop(0)

            if x >= 0:
                if len(rs_right) == x:
                    rs_right.append([])


                rs_right[x].append((n.val, y))
            else:
                _x = abs(1+x)
                if len(rs_left) == _x:
                    rs_left.append([])

                rs_left[_x].append((n.val, y))

            if n.left:
                q.append((n.left, x-1, y+1))

            if n.right:
                q.append((n.right, x+1, y+1))

        rs = []
        for li in rs_left[::-1]:
            li.sort(key=lambda x: (x[1], x[0]))
            rs.append([x[0] for x in li])

        for li in rs_right:
            li.sort(key=lambda x: (x[1], x[0]))
            rs.append([x[0] for x in li])

        return rs


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    s = Solution()
    rs = s.verticalTraversal(n1)
    print(rs)
