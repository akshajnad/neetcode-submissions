# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find(curr, path, end):
            if not curr:
                path.append(None)
                return
            path.append(curr)
            if curr.val == end.val:
                return
            if curr.val > end.val:
                find(curr.left, path, end)
            else:
                find(curr.right, path, end)
        path1 = []
        path2 = []
        find(root, path1, p)
        find(root, path2, q)
        result = root
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                result = path1[i]
            else:
                return result
        return result