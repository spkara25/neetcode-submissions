class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        j = 0
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i] == nums[j]):
                    return True
        return False