class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return 0
            if rank[n1] > rank[n2]:
                par[n2] = par[n1]
                rank[n1] += rank[n2]
            else:
                par[n1] = par[n2]
                rank[n2] += rank[n1]
            return 1
        for edge in edges:
            n -= union(edge[0], edge[1])
        return n