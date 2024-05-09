class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        ans = 0
        while right < len(nums) - 1:
            maxIdx = 0
            for i in range(left, right+1):
                maxIdx = max(maxIdx, i + nums[i])
            left = right+1
            right = maxIdx
            ans+=1
        return ans