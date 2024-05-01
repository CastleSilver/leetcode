class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #맨 뒤에건 생략
        index = len(nums) - 2
        st = nums[index+1]
        k = 1
        while index >= 0:
            if nums[index] == st:
                del nums[index]
            else:
                st = nums[index]
                k += 1
            index -= 1
        return k