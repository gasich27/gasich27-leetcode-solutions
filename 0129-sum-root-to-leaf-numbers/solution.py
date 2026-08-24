# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def dfs(node, res):
            if node.left is None and node.right is None:
                res += str(node.val)
                result.append(int(res))
                return

            res += str(node.val)

            if node.left:
                dfs(node.left, res)

            if node.right:
                dfs(node.right, res)

        dfs(root, '')
        return sum(result)

