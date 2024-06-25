# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
            else:
                return False
        if root.left is not None and root.right is not None:
            return self.getSum(root.left, targetSum, root.val) or self.getSum(root.right, targetSum, root.val)
        elif root.left is None:
            return self.getSum(root.right, targetSum, root.val)
        elif root.right is None:
            return self.getSum(root.left, targetSum, root.val)
    
    def getSum(self, node: Optional[TreeNode], targetSum, curSum) -> bool:
        if node.left is None and node.right is None:
            if curSum + node.val == targetSum:
                return True
            else:
                return False
        if node.left is None:
            return self.getSum(node.right, targetSum, curSum + node.val)
        if node.right is None:
            return self.getSum(node.left, targetSum, curSum + node.val)
        return self.getSum(node.left, targetSum, curSum + node.val) or self.getSum(node.right, targetSum, curSum + node.val)