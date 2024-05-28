# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.buildBST(nums, 0, len(nums) - 1)
    
    def buildBST(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildBST(nums, left, mid - 1)
        node.right = self.buildBST(nums, mid + 1, right)
        return node
        
            