class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        fresh = 0
        queue = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                val = grid[r][c]
                if val == 2:
                    queue.append((r, c))
                elif val == 1:
                    fresh += 1
        
        time = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        while queue and fresh > 0:
            oranges = []
            while queue:
                popped = queue.pop()
                oranges.append(popped)
                visited.add(popped)
            for orange in oranges:
                for dr, dc in directions:
                    nr = orange[0] + dr
                    nc = orange[1] + dc
                    if not ((nr, nc) in visited or nr < 0 or nr > len(grid) - 1 or nc < 0 or nc > len(grid[nr]) - 1 or grid[nr][nc] != 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1