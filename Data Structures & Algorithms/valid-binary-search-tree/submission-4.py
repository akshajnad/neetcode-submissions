# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(curr):
            if curr:
                inorder(curr.left)
                path.append(curr.val)
                inorder(curr.right)
        path = []
        inorder(root)
        return path == sorted(path) and len(set(path)) == len(path)