"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        q = deque()
        q.append((root, 0))
        while q:
            cur, level = q.popleft()
            if q:
                tmp, tmpLevel = q.popleft()
                if level == tmpLevel:
                    cur.next = tmp
                q.appendleft((tmp, tmpLevel))
            if cur.left:
                q.append((cur.left, level+1))
            if cur.right:
                q.append((cur.right, level+1))
        
        return root