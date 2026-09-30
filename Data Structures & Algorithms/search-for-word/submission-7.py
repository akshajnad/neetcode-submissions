class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if (r < 0 or r > len(board)-1 or c < 0 or c > len(board[r])-1 or (r, c) in visited or found[0] or board[r][c] != word[i]):
                return
            
            if i == len(word) - 1:
                found[0] = True
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, i+1)
            visited.remove((r, c))
        
        found = [False]
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    visited.clear
                    dfs(r, c, 0)
                if found[0]:
                    return True

        return False
