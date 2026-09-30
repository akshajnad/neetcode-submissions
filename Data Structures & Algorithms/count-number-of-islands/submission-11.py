class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[r])-1 or (r, c) in visited or grid[r][c] == "0"):
                return
            visited.add((r, c))
            #grid[r][c] = 0
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        visited = set()
        num = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num += 1
                    dfs(r, c)

        return num
