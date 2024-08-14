from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # 배열을 정렬합니다.
        
        # 가능한 최소 거리와 최대 거리
        left, right = 0, nums[-1] - nums[0]
        
        # 이진 탐색을 통해 k번째로 작은 거리를 찾습니다.
        while left < right:
            mid = (left + right) // 2
            
            # mid 이하의 거리를 가진 쌍의 개수를 셉니다.
            if self._count_pairs(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
                
        return left

    def _count_pairs(self, nums: List[int], max_distance: int) -> int:
        count = 0
        left = 0
        
        # 두 포인터를 이용하여 쌍의 개수를 셉니다.
        for right in range(len(nums)):
            while nums[right] - nums[left] > max_distance:
                left += 1
            count += right - left
            
        return count

        