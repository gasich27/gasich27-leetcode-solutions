# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0, True

            r_depth, r_balans = dfs(node.right)
            l_depth, l_balans = dfs(node.left)

            if r_balans and l_balans and (-1 <= r_depth - l_depth <= 1):
                return max(r_depth, l_depth) + 1, True

            return 0, False

        return dfs(root)[1]
