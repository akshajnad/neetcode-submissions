class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    for i in range(len(matrix[r])):
                        if matrix[r][i] != 0:
                            matrix[r][i] = "a"
                    for i in range(len(matrix)):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "a"
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == "a":
                    matrix[r][c] = 0        