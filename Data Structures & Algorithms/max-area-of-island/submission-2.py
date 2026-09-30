class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[r])-1 or (r, c) in visited or grid[r][c] == 0):
                return 0
            visited.add((r, c))
            result = 1
            for dr, dc in directions:
                result += dfs(r+dr, c+dc)
            return result

        sizes = [0]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    sizes.append(dfs(r, c))
        return max(sizes)