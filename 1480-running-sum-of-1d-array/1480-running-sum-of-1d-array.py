class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        plus = 0
        for i in nums:
            plus += i
            ans.append(plus)
        
        return ans