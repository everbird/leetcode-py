#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    max_depth = 0
    nodes = []
    def subtreeWithAllDeepest(self, root):
        self.max_depth = 0
        self.nodes = []
        self.dfs(root)

        def lca(a, b):
            if not a:
                return b

            if not b:
                return a

            path_a = set([])
            while a:
                path_a.add(a)
                a = a.parent

            while b:
                if b in path_a:
                    return b
                b = b.parent

        return reduce(lca, self.nodes)


    def dfs(self, node, deepth=0, parent=None):
        if not node:
            return

        node.parent = parent

        if deepth > self.max_depth:
            self.max_depth = deepth
            self.nodes = [node]
        elif deepth == self.max_depth:
            self.nodes.append(node)


        self.dfs(node.left, deepth+1, node)
        self.dfs(node.right, deepth+1, node)





def binary_tree_to_list(root):
    r = []
    q = [root]
    target_length = length = 0
    while q:
        n = q.pop()
        length += 1
        if n:
            r.append(n.val)
            target_length = length
        else:
            r.append(None)

        if n:
            q = [n.right, n.left] + q

    return r[:target_length]


def list_to_binary_tree(values):
    len_n = len(values)
    root = TreeNode(values[0])
    q = [root]
    for i in range(1, len_n, 2):
        n = q.pop()
        v = values[i]
        left = TreeNode(v) if v else None
        n.left = left
        if left:
            q = [left] + q
        if i+1 < len_n:
            v = values[i+1]
            right = TreeNode(v) if v else None
            n.right = right
            if right:
                q = [right] + q
    return root


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode(val={})>'.format(self.val)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            list_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4]),
            [2,7,4]
        ),
        (
            list_to_binary_tree([1]),
            [1]
        ),
    ]
    for input_args, expected in tests:
        r = s.subtreeWithAllDeepest(input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
