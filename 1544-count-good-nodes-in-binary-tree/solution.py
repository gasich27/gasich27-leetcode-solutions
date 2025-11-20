# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            if not node:
                return 0
            
            count = 0
            if node.val >= current_max:
                count = 1
                current_max = node.val

            left_count = dfs(node.left, current_max)
            right_count = dfs(node.right, current_max)
            
            return count + left_count + right_count

        return dfs(root, root.val)
