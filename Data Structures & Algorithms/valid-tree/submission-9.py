class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        def dfs(curr, prev):
            visited.add(curr)
            result[1] += 1
            for n in adjList[curr]:
                if n != prev:
                    if n in visited:
                        result[0] = False
                        return
                    else:
                        dfs(n, curr)
        result = [True, 0]
        visited = set()
        dfs(0, -1)
        if result[1] != n:
            result[0] = False
        return result[0]