import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if target > sum(nums):
            return 0
        
        minLength = float('inf')
        curSum = 0
        curLength = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            curLength += 1
            while curSum >= target:
                minLength = min(minLength, curLength)
                curSum -= nums[i-curLength+1]
                curLength -= 1
                
            
        return minLength