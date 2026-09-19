class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap ={}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) +1
        sorted_keys = sorted(hashmap.keys(), key = lambda x: hashmap[x], reverse = True)

        return sorted_keys[:k]
            