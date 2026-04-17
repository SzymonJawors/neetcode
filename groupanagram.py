from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    
    for s in strs:
        sorted_s = "".join(sorted(s))
        
        res[sorted_s].append(s)
        
    
    return list(res.values())


strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))
