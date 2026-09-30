# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            def levelorder(start):
                queue = deque()
                queue.append(start)
                arr = []
                while queue:
                    curr = queue.popleft()
                    arr.append(curr.val if curr else None)
                    if curr:
                        queue.append(curr.left)
                        queue.append(curr.right)
                return arr
            
            return levelorder(p) == levelorder(q)
        def preorder(curr):
            if same(curr, subRoot):
                return True
            if not curr:
                return False
            return preorder(curr.left) or preorder(curr.right)
        return preorder(root)