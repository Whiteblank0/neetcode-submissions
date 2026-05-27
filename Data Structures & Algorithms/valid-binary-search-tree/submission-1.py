# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node is None:
                return float('inf'), float('-inf')
            l_min, l_max = f(node.left)
            r_min, r_max = f(node.right)
            x = node.val
            if x <= l_max or x >= r_min:
                return float('-inf'), float('inf')
            return min(l_min, x), max(r_max, x)
        return f(root)[1] != float('inf')
            