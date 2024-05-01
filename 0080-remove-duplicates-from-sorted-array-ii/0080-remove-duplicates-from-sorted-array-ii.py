class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1 # 중복 수 기록
        index = len(nums) - 2 # 맨 뒤는 제외
        st = nums[index + 1] # 맨 뒤 숫자를 초기 숫자로
        while index >= 0:
            if st == nums[index]:
                if cnt >= 2:
                    del nums[index]
                else:
                    cnt+=1
            else:
                st = nums[index]
                cnt = 1
            index -= 1
            
        