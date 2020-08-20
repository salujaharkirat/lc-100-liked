# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)
        
        return max(l_height, r_height) + 1
