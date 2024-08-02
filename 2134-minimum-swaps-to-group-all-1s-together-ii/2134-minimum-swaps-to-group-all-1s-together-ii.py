import math

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = sum(nums)
        
        #swap이 필요없는 경우
        if totalOnes == 0 or totalOnes == len(nums):
            return 0
        
        extendedNums = nums + nums
        maxOnesInWindow = 0
        curOnesInWindow = 0
        
        #첫번째 윈도우 값 구하기
        for i in range(totalOnes):
            if nums[i] == 1:
                curOnesInWindow += 1
        
        maxOnesInWindow = curOnesInWindow
        
        #윈도우 이동
        for i in range(totalOnes, len(extendedNums)):
            if extendedNums[i] == 1:
                curOnesInWindow += 1
            if extendedNums[i - totalOnes] == 1:
                curOnesInWindow -= 1
            maxOnesInWindow = max(maxOnesInWindow, curOnesInWindow)
        
        return totalOnes - maxOnesInWindow