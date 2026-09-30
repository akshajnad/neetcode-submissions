# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, path, curr):
            if curr == None:
                return
            path.append(curr)
            if curr.val < node.val:
                dfs(node, path, curr.right)
            elif curr.val > node.val:
                dfs(node, path, curr.left)
            else:
                return
        
        p1 = []
        p2 = []
        dfs(p, p1, root)
        dfs(q, p2, root)
        p2 = set(p2)
        for i in range(len(p1)-1, -1, -1):
            if p1[i] in p2:
                return p1[i]
        
        return root
