class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = {i:[] for i in range(numCourses)}
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        result = []
        def dfs(curr):
            if curr not in graph:
                return
            if curr in visited:
                result.append(False)
                return
            visited.add(curr)
            for nbr in graph[curr]:
                dfs(nbr)
            visited.remove(curr)
            graph[curr] = []
        for pair in prerequisites:
            visited = set()
            dfs(pair[0])
            if len(result) == 1:
                return False
        return True