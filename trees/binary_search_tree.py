def tree_search(root, target):

    if not root:
        return False

    if target > root.val:
        return tree_search(root.right, target)

    elif target < root.val:
        return tree_search(root.left, target)

    else:
        return True
