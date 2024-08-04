class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_arrays = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                sub_arrays.append(sum)
        sub_arrays.sort()
        
        range_sum = 0
        mod = 10**9 + 7
        for i in range(left-1, right):
            range_sum = (range_sum + sub_arrays[i]) % mod
        return range_sum