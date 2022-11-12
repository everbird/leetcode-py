#!/usr/bin/env python3

class Solution:
    result = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        cache = {0: 1}
        def dfs(node, current_sum):
            if not node:
                return

            current_sum += node.val
            old_sum = current_sum - target
            self.result += cache.get(old_sum, 0)
            cache[current_sum] = cache.get(current_sum, 0) + 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Don't forget to retrieve back, since need to revert the number when leaving the branch
            cache[current_sum] -= 1

        dfs(root, 0)
        return self.result
