# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []
        def inorder(curr):
            if curr == None:
                return
            inorder(curr.left)
            traversal.append(curr.val)
            inorder(curr.right)
        
        inorder(root)
        if len(set(traversal)) < len(traversal):
            return False

        return traversal == sorted(traversal)