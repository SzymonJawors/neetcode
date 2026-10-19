import heapq

def kClosest(points, k):
    """Return the ``k`` points closest to the origin."""
    min_heap = []
    for x, y in points:
        dist = (x**2) + (y**2)
        min_heap.append((dist, x, y))
        
    heapq.heapify(min_heap)
    res = []
    for _ in range(k):
        dist,x,y = heapq.heappop(min_heap)
        res.append([x,y])
    
    return res