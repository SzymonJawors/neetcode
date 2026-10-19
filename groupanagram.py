from collections import defaultdict

def groupAnagrams(strs):
    """Group strings that share the same letters and return the groups."""
    res = defaultdict(list)
    
    for s in strs:
        sorted_s = "".join(sorted(s))
        
        res[sorted_s].append(s)
        print(list(res))
        
    
    return list(res.values())


strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))
