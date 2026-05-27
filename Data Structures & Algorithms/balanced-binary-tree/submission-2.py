# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkDepth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = checkDepth(node.left)
            if left == -1:
                return -1
            
            right = checkDepth(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        return checkDepth(root) != -1