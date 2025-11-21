# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        def tot(node, cur):
            if not node:
                return 

            if cur + node.val == targetSum:
                self.total += 1
            
            tot(node.left, cur + node.val)
            tot(node.right, cur + node.val)


        def dfs(node):
            if not node:
                return 
            
            tot(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.total
