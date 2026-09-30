class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        visited = set()
        visited.add((0, 0))
        result = [matrix[0][0]]
        done = False
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r = 0
        c = 0
        while not done:
            direc = directions[d]
            nr = r + direc[0]
            nc = c + direc[1]
            if (nr, nc) in visited or nr > len(matrix) - 1 or nr < 0 or nc > len(matrix[nr]) - 1 or nc < 0:
                d = (d + 1) % 4
                direc = directions[d]
                nr = r + direc[0]
                nc = c + direc[1]
                if (nr, nc) in visited or nr > len(matrix) - 1 or nr < 0 or nc > len(matrix[nr]) - 1 or nc < 0:
                    done = True
                    break
            r = nr
            c = nc
            visited.add((nr, nc))
            result.append(matrix[nr][nc])
        
        return result
            