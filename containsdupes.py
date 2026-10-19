def containdupes(nums):
    """Return whether ``nums`` contains any repeated value."""
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False