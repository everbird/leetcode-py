#!/usr/bin/env python3

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return to_bst(nums, 0, len(nums)-1)

def to_bst(nums, s, e):
    if s > e:
        return

    if s == e:
        return TreeNode(nums[s])

    m = (s - e) // 2 + e
    left = to_bst(nums, s, m-1)
    right = to_bst(nums, m+1, e)
    n = TreeNode(nums[m])
    n.left = left
    n.right = right
    return n
