def findOrder(numCourses, prerequisites):
    """Return a valid course order, or an empty list when prerequisites cycle."""
    preMap = {i: [] for i in range(numCourses)}
    
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
        
    res = []
    
    visit, cycle = set(), set()
    
    def dfs(crs):
        # ``cycle`` is the active recursion path; ``visit`` caches completed courses.
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        
        cycle.remove(crs)
        visit.add(crs)
        res.append(crs)
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return []
    return res