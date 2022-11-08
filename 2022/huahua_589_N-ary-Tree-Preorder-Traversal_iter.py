class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        s = [root]
        rs = []

        while s:
            n = s.pop()
            rs.append(n.val)

            for c in n.children[::-1]:
                if c:
                    s.append(c)

        return rs
