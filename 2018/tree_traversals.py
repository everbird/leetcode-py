def inorder_iterative(head):
    s = [head]

    while head and s:
        if head.left:
            s.append(head.left)
            head = head.left
        else:
            head = s.pop()
            print head.val
            if head.right:
                s.append(head.right)
                head = head.right

def preorder_iterative(head):
    s = [head]

    while head and s:
        head = s.pop()
        print head.val
        if head.right:
            s.append(head.right)

        if head.left:
            s.append(head.left)

def postorder_iterative(head):
    if not head:
        return

    s = []

    while head or s:

        if head:
            s.append(head)
            head = head.left
        else:
            head = s[-1]
            if head.right and flag != head.right:
                s.append(head.right)
                head = head.right.left
            else:
                head = s.pop()
                print head.val
                flag = head
                head = None  # Goto head = s[-1, when it returns from right, avoid to go to right again.]



class TreeNode(object):
    left = None
    right = None

    def __init__(self, val):
        self.val = val


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

h = a
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

inorder_iterative(h)
print '-'*10
preorder_iterative(h)
print '-'*10
postorder_iterative(h)
