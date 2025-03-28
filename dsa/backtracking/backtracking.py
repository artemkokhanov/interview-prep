class TreeNode:
    def __init__(self):
        self.val = None
        self.right = None
        self.left = None


def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:  # root has no children, i.e., found leaf node
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False


def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
