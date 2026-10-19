def maxArea(height):
    """Return the maximum area formed by two vertical lines."""
    res = 0
    l,r =0, len(height) -1
    
    while l < r:
        width = r - l
        
        h = min(height[l], height[r])
        
        area = width * h
        
        res = max(res, area)
        
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    
    return res