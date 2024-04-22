from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        length = len(board)

        board.reverse()
        # Define a method to convert the square to (r, c) co-ordinates
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2: 
                # This is an alternate row (let's flip the columns)
                c = length - 1 - c
            return [r, c]
        

        # Initialize the queue and the seen set
        queue = deque([[1, 0]])
        seen = set()

        while queue:

            # Get the current square
            square, moves = queue.popleft()

            for i in range(1, 7):

                next_square = square + i
                r, c = intToPos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length * length:
                    return moves + 1
                if next_square not in seen:
                    seen.add(next_square)
                    queue.append([next_square, moves + 1])
        
        return -1
