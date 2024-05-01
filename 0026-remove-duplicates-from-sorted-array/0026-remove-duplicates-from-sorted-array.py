class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preNum = nums[0]
        k = 1
        
        for n in range(1, len(nums)):
            if preNum == nums[k]:
                del nums[k]
                k -= 1
            else:
                preNum = nums[k]
            k += 1
        return k
                