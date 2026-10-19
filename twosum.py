def twosum(nums, target):
    """Return indices of two values that sum to ``target``."""
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i