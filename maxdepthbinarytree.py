def maxDepth(root):
    if not root:
        return 0
    
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)
    
    return 1 + max(left_height, right_height)