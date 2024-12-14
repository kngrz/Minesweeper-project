import random 

class Minesweeper: 
    def __init__(self, r, c, mines): 
        self.r = r 
        self.c = c
        self.mines = mines
        self.real_board = None
        self.player_board = None
        self.player_total_spaces = (self.r * self.c) - self.mines
    
    def create_board(self): 
        self.real_board = [['_' for i in range(self.c)] for j in range(self.r)] 
        self.player_board = [['x' for i in range(self.c)] for j in range(self.r)] 

        count_mines = 0    
        while count_mines != self.mines:
            r_row = random.randrange(self.r) 
            r_col = random.randrange(self.c) 

            if self.real_board[r_row][r_col] != 'X': 
                self.real_board[r_row][r_col] = 'X'
                count_mines += 1
            else: 
                continue

    def set_board(self, zeros=False): 
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1), (-1, 1)] 

        for r in range(self.r): 
            for c in range(self.c): 
                if self.real_board[r][c] == 'X': 
                    continue 

                mine_count = 0 
                for d in directions: 
                    rd = r + d[0]
                    cd = c + d[1] 
                    if rd >= 0 and rd < self.r and cd >= 0 and cd < self.c: 
                        if self.real_board[rd][cd] == 'X': 
                            mine_count += 1
                
                self.real_board[r][c] = str(mine_count)
        
        x, y = self.first_move() 
        self.player_board[x][y] = self.real_board[x][y]

        if zeros: 
            self.remove_zeros(x, y) 
    
    def remove_zeros(self, r, c): 
        visited = set((r,c))  
        def _dfs(r, c):
            directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1), (-1, 1)] 

            for d in directions: 
                rd = r + d[0]
                cd = c + d[1] 

                if rd >= 0 and rd < self.r and cd >= 0 and cd < self.c \
                    and self.real_board[rd][cd] == '0' and (rd, cd) not in visited: 
                    self.player_board[rd][cd] = self.real_board[rd][cd] 
                    self.player_total_spaces -= 1
                    visited.add((rd, cd)) 
                    _dfs(rd, cd) 
        _dfs(r, c) 

    def print_board(self, debug=True):  
        if not debug: 
            for r in self.real_board: 
                for items in r: 
                    print(f'{items} | ', end = "") 
                print()
        else: 
            for r in self.player_board: 
                for items in r: 
                    print(f'{items} | ', end = "") 
                print()
    
    def first_move(self): 
        start_r = random.randrange(self.r) 
        start_c = random.randrange(self.c) 

        while self.real_board[start_r][start_c] != '0': 
            start_r = random.randrange(self.r) 
            start_c = random.randrange(self.c) 

        return (start_r, start_c) 
        
    def run_game(self): 
        self.create_board()
        self.set_board()
        self.print_board() 

        while True: 
            user_input = input().split() 
            if len(user_input) != 2: 
                print("Wrong input, try again.") 
                continue
            elif not user_input[0].isdigit() or not user_input[1].isdigit(): 
                print("Wrong input, try again.") 
                continue
            
            x, y = int(user_input[0]), int(user_input[1])
            if self.real_board[x][y] == 'X': 
                print() 
                print("Game over.") 
            else: 
                self.player_board[x][y] = self.real_board[x][y]
                self.player_total_spaces -= 1
            
            if self.player_total_spaces == 0: 
                print() 
                self.print_board(True)
                print("You win.") 
                return 

            self.print_board(True) 
