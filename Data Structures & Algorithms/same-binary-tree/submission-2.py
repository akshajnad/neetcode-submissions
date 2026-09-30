# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(start):
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
        
        return inorder(p) == inorder(q)