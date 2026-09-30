# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level = []
            while queue:
                level.append(queue.popleft())
            for i in range(len(level)):
                if level[i].left: 
                    queue.append(level[i].left)
                if level[i].right: 
                    queue.append(level[i].right)
                level[i] = level[i].val
            result.append(level)
        return result
