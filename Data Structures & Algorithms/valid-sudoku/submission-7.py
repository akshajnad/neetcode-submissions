class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rc = set()
        for r in board:
            for c in r:
                if c in rc:
                    return False
                elif c != ".":
                    rc.add(c)
            rc.clear()
        
        for c in range(len(board[0])):
            for r in board:
                if r[c] in rc:
                    return False
                elif r[c] != ".":
                    rc.add(r[c])
            rc.clear()

        boxes = {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                key = (r//3, c//3)
                box = boxes.get(key, set())
                if board[r][c] in box:
                    return False
                elif board[r][c] != ".":
                    box.add(board[r][c])
                boxes[key] = box
        
        return True