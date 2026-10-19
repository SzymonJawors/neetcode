def invertTree(root):
    """Invert a binary tree in place and return its root."""
    if not root:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    invertTree(root.left)
    invertTree(root.right)

    return root