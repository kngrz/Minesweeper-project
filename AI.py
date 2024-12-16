from collections import deque
from Constants import Constants

class My_AI(): 
    def __init__(self, x, y, mines, board): 
        self.x = x
        self.y = y 
        self.board = board
        self.mines_count = mines
        self.safe_frontier = deque() 
        self.unsure_frontier = deque()  
        self.mines = deque() 

        self.directions = [
            (0,1), (0,-1), (1,0), (-1,0), 
            (1,1), (1,-1), (-1,-1), (-1, 1)
            ] 
    
    def add_neighbors(self, x, y, frontier): 
        for dir in self.directions: 
            row_dir = x + dir[0]
            col_dir = y + dir[1]

            if (
                row_dir >= 0 and row_dir < self.x and 
                col_dir >= 0 and col_dir < self.y and
                self.board[row_dir][col_dir] == Constants.SPACE and 
                (row_dir, col_dir) not in frontier
            ): 
                frontier.append((row_dir, col_dir))

# fix heuristic and trying to function + frontier appends
    def play_move(self, x, y, res): 
        self.board[x][y] = res

        if res == Constants.ZERO_TILE: 
            ...





            
            



        
            



