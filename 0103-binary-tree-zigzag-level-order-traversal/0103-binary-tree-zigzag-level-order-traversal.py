# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        level = 0
        while queue:
            size = len(queue)
            nodes = []
            
            for i in range(size):
                if level%2 == 0:
                    node = queue.popleft()
                else:
                    node = queue.pop()
                nodes.append(node.val)
                if level % 2 == 0:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            ans.append(nodes)
            level += 1
        return ans