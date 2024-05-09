class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 0
        mp = 0
        if l==1:
            return 0
        ans = 0
        memo = [0]
        while i <= mp:
            if i+nums[i]>mp and i+nums[i]>memo[-1]:
                memo.append(i+nums[i])
            if i == mp:
                mp = memo[-1]
                ans += 1
            if mp>=l-1:
                return ans
            i += 1