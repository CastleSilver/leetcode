# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = 0
        arr = collections.deque()
        arr.append(head)
        while arr:
            node = arr.popleft()
            end += 1
            if node.next:
                arr.append(node.next)
        
        middle = end//2 + 1
        arr.append(head)
        while middle > 0:
            middle -= 1
            node = arr.popleft()
            if middle == 0:
                return node
            if node.next:
                arr.append(node.next)