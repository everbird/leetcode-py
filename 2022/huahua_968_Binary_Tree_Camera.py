#!/usr/bin/env python3

from enum import Enum

class State(Enum):
    NONE = 0
    COVERED = 1
    CAMERA = 2

class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        r = 0
        def dfs(node: TreeNode) -> int:
            nonlocal r
            if not node:
                return State.COVERED

            left = dfs(node.left)
            right = dfs(node.right)
            if left == State.NONE or right == State.NONE:
                r += 1
                return State.CAMERA

            elif left == State.CAMERA or right == State.CAMERA:
                return State.COVERED

            return State.NONE

        if dfs(root) == State.NONE:
            r += 1

        return r
