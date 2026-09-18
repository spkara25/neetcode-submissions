class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        acSum = 0
        arSum = 0

        for i in range (len(nums)+1):
            acSum += i
        
        for i in range(len(nums)):
            arSum += nums[i]
        
        return acSum - arSum