def twoSum(numbers, target):
    """Return one-based indices of two sorted values that sum to ``target``."""
    l = 0
    r = len(numbers) - 1
    while l < r:
        twosum = numbers[l] + numbers[r]
        if twosum > target:
            r-=1
        elif twosum < target:
            l+=1
        else:
            return [l+1, r+1]