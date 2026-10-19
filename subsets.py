def subsets(nums):
    """Return all subsets of ``nums``."""
    res = []
    subset = []
    def dfs(i):
        # Each input value creates two branches: include it or skip it.
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        subset.append(nums[i])
        dfs(i + 1)
        
        subset.pop()
        dfs(i + 1)
    
    dfs(0)
    return res