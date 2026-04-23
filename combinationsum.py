def combinationSum(candidates, target):
    res = []
    subset = []
    def dfs(i, current_total):
        if current_total == target:
            res.append(subset.copy())
            return
        if i >= len(candidates) or current_total > target:
            return
        subset.append(candidates[i])
        dfs(i, current_total + candidates[i])
        
        subset.pop()
        dfs(i + 1, current_total)
    dfs(0,0)
    return res