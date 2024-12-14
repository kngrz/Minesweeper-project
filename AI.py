from collections import deque

class My_AI(): 
    def __init__(self): 
        self.board = None
        self.zero_frontier = deque() # 
        self.num_frontier = deque()  
        # self.flags = 0

    def set_board(self, board): 
        self.board = board  
    
    def play_move(self, r, c, res): 
        self.board[r][c] = res 
        ...

        






    

    