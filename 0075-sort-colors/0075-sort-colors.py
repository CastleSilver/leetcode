class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for num in nums:
            count[num] = count[num] + 1
        
        color = 0
        idx = 0
        while idx < len(nums):
            if count[color] == 0:
                color = color + 1
                continue
            nums[idx] = color
            count[color] = count[color] - 1
            idx = idx + 1

