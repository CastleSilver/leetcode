import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min-heap of size k
        heap = nums[:k]
        heapq.heapify(heap)  # Convert the first k elements into a heap
        
        for num in nums[k:]:
            if num > heap[0]:  # If the current number is larger than the smallest in the heap
                heapq.heappushpop(heap, num)  # Push the current number and pop the smallest
        
        return heap[0]  # The root of the heap is the k-th largest element

        