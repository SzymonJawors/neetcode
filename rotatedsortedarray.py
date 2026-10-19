def search(nums, target):
    """Return ``target``'s index in a rotated sorted array, or ``-1``."""
    l,r = 0, len(nums) -1
    
    while l <=r:
        mid = (l+r) // 2
        if target == nums[mid]:
            return mid
        
        # At least one half remains sorted; restrict the search to the half
        # that can contain the target.
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid +1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid -1
            else:
                l = mid +1
    return -1