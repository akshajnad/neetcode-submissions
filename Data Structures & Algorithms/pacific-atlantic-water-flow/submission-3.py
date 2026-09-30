class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(r, c):
            cells = []
            queue = collections.deque()
            visited = set()
            queue.append((r, c))
            while queue:
                curr = queue.popleft()
                r = curr[0]
                c = curr[1]
                visited.add(curr)
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if not ((nr, nc) in visited or nr < 0 or nr > len(heights) - 1 or nc < 0 or nc > len(heights[r]) - 1):
                        if heights[nr][nc] >= heights[r][c]:
                            queue.append((nr, nc))
                cells.append((r, c))
            
            return cells
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = []
        atlantic = []
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if r == 0 or c == 0:
                    pacific.extend(bfs(r, c))
                if r == len(heights) - 1 or c == len(heights[r]) - 1:
                    atlantic.extend(bfs(r, c))
        
        result = list(set(pacific).intersection(set(atlantic)))
        result = [list(i) for i in result]
        return result