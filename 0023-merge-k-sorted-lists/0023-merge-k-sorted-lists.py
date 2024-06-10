# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # 각 리스트의 첫 번째 노드를 힙에 추가
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            # 힙에서 가장 작은 값을 꺼냄
            val, i, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next

            # 다음 노드가 있다면 힙에 추가
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next