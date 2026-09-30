# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return -1
            return max(height(node.left), height(node.right)) + 1
        def dfs(curr):
            if not curr:
                return
            if abs(height(curr.left) - height(curr.right)) > 1:
                balanced.append(False)
                return
            dfs(curr.left)
            dfs(curr.right)
        balanced = []
        dfs(root)
        return len(balanced) == 0