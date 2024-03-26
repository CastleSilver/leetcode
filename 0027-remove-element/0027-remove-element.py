class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        index = len(nums) - 1
        while index >= 0 :
            if nums[index] == val :
                del nums[index]
            else:
                k += 1
            index -= 1
        return k