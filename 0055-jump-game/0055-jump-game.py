class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0] == 0 and len(nums) > 1:
            return False
        
        result = True
        zeroIdx = -1
        for i in range(len(nums) - 2, -1, -1):
            if zeroIdx >= 0:
                if zeroIdx - i >= nums[i]:
                    result = False
                else:
                    zeroIdx = -1
                    result = True
            if nums[i] == 0 and zeroIdx < 0:
                zeroIdx = i
        
        return result
                
        