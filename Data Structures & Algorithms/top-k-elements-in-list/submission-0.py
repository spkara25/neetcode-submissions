class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res =[]
        hashmap = {}
        count = 0
        for i, a in enumerate(nums):
            if a in hashmap:
                if hashmap.get(a) < k:
                    res.append(a)
                    count += 1
            hashmap[a] = count
        return res
            