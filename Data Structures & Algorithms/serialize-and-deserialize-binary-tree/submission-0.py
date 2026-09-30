# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(curr):
            if not curr:
                result.append("N")
                return
            result.append(str(curr.val))
            preorder(curr.left)
            preorder(curr.right)
        result = []
        preorder(root)
        return ";".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(";")
        self.i = 0
        def dfs():
            if preorder[self.i] == "N":
                self.i += 1
                return None
            curr = TreeNode(int(preorder[self.i]))
            self.i += 1
            curr.left = dfs()
            curr.right = dfs()
            return curr
        return dfs()
