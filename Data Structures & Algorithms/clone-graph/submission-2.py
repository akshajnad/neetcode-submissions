"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque()
        visited = set()
        queue.append(node)
        hashmap = {}
        result = []
        while queue:
            curr = queue.popleft()
            add = Node(curr.val)
            hashmap[curr] = add
            visited.add(curr)
            result.append(add)
            for n in curr.neighbors:
                if n not in visited:
                    queue.append(n)
        for old in hashmap:
            for n in old.neighbors:
                hashmap[old].neighbors.append(hashmap[n])
        return result[0]