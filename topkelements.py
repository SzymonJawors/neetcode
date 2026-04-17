def topKFrequent(nums,k):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    freq = [[] for i in range(len(nums) + 1)]
        
    for n, c in count.items():
            freq[c].append(n)
                
    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent([1,1,3,4,5,2,3,3,4,1,1,5,5,5], 3))