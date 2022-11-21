#!/usr/bin/env python3

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return delete(root, key)


def delete(root, key):
    # find
    parent_path = (None, None)  # 0: left, 1:right
    p = root
    while p and p.val != key:
        if key < p.val:
            parent_path = (p, 0)
            p = p.left
        elif key > p.val:
            parent_path = (p, 1)
            p = p.right

    if not p:
        return root

    _p, _path = parent_path

    # case 1&2: no left or right or both
    flag = False
    if not p.left and not p.right:
        new_node = None
        flag = True
    if not p.left:
        new_node = p.right
        flag = True
    elif not p.right:
        new_node = p.left
        flag = True

    if flag:
        if _path == 0:
            _p.left = new_node
        elif _path == 1:
            _p.right = new_node

        return root if _p else new_node

    # case 3: find smallest from right
    pre = None
    rp = p.right
    while rp.left:
        pre = rp
        rp = rp.left

    print(">>>", pre, rp)
    if pre:
        pre.left = rp.right

    if p.right != rp:
        rp.right = p.right

    if p.left != rp:
        rp.left = p.left

    if _path == 0:
        _p.left = rp
    elif _path == 1:
        _p.right = rp

    return root if _p else rp
