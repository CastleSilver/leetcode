class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == k:
            return
        copyNums = nums[:]
        for n in range(0, length):
            nums[(n+k)%length] = copyNums[n]