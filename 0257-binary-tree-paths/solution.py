# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, string):
            if node.left is None and node.right is None:
                string += str(node.val)
                res.append(string)
                return
            
            string += str(node.val) + '->'

            if node.left:
                dfs(node.left, string)
            
            if node.right:
                dfs(node.right, string)

        dfs(root, '')
        return res
