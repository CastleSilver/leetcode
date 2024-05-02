class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)/2
        cnt = dict()
        result = 0
        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
                
            if cnt[n] > length:
                result = n
                break;
                
        return result