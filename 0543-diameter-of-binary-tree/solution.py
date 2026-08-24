# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diametr = 0
        def dfs(node):
            nonlocal diametr
            if not node:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)

            diametr = max(diametr, right + left)
            return max(left, right) + 1
        
        dfs(root)
        return diametr
