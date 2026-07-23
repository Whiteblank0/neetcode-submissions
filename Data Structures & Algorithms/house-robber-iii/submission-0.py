# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0,0
            l_rob, l_not = dfs(node.left)
            r_rob, r_not = dfs(node.right)
            rob = l_not + r_not + node.val
            not_rob = max(l_rob, l_not) + max(r_rob, r_not)
            return rob, not_rob
        return max(dfs(root))