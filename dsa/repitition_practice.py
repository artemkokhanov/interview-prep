class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, target):
    if not root:
        return False

    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else:
        return True


def insert(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def minValueNode(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr


def remove(root, val):
    if not root:
        return None

    if val < root.val:
        root.left = remove(root.left, val)
    elif val > root.val:
        root.right = remove(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
