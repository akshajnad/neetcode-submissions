# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(curr):
            if curr:
                inorder(curr.left)
                path.append(curr.val)
                inorder(curr.right)
        path = []
        inorder(root)
        return path[k-1]