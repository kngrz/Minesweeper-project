import random 
import os
import AI

def clear_console(): 
    clear = lambda: os.system('cls')
    return clear() 

class Minesweeper: 
    MINE = 'X'
    SPACE = ' '
    EMPTY_TILE = '0'
    FLAG = 'F' 

    def __init__(self, r=8, c=8, mines=10): 
        self.r = r 
        self.c = c
        self.mines = mines
        self.real_board = None
        self.player_board = None
        self.player_total_spaces = (self.r * self.c) - self.mines

    def create_board(self): 
        """ Create self.r x self.c array 
        """

        self.real_board = [['_' for i in range(self.c)] for j in range(self.r)] 
        self.player_board = [[' ' for i in range(self.c)] for j in range(self.r)] 

        count_mines = 0    
        while count_mines != self.mines:
            r_row = random.randrange(self.r) 
            r_col = random.randrange(self.c) 

            if self.real_board[r_row][r_col] != self.MINE: 
                self.real_board[r_row][r_col] = self.MINE
                count_mines += 1
            else: 
                continue

    def set_board(self): 
        directions = [
            (0,1), (0,-1), (1,0), (-1,0), 
            (1,1), (1,-1), (-1,-1), (-1, 1)
            ] 

        for r in range(self.r): 
            for c in range(self.c): 
                if self.real_board[r][c] == self.MINE: 
                    continue 

                mine_count = 0 
                for d in directions: 
                    rd = r + d[0]
                    cd = c + d[1] 
                    if rd >= 0 and rd < self.r and cd >= 0 and cd < self.c: 
                        if self.real_board[rd][cd] == self.MINE: 
                            mine_count += 1
                
                self.real_board[r][c] = str(mine_count)
        
        x, y, result = self.first_move() 
        self.player_board[x][y] = result

    def print_board(self, debug=True):  
        clear_console() 
        if debug is False: 
            for r in self.real_board: 
                for items in r: 
                    print(f'{items}', end = "") 
                print()
        else: 
            for i in range(self.r): 
                print(f'{i} ', end = "") 
                for items in self.player_board[i]: 
                    print(f'[{items}]', end = "") 
                print() 

            print("   ", end = "") 
            for j in range(self.c): 
                print(f'{str(j)}  ', end = "") 
            print() 
              
    def first_move(self): 
        start_r = random.randrange(self.r) 
        start_c = random.randrange(self.c) 

        while self.real_board[start_r][start_c] != self.EMPTY_TILE: 
            start_r = random.randrange(self.r) 
            start_c = random.randrange(self.c) 

        return (start_r, start_c, self.real_board[start_r][start_c]) 
        
    def run_game(self): 
        self.create_board()
        self.set_board()
        self.print_board() 

        while True: 
            user_input = input().split() 
            if len(user_input) == 3:
                x, y = int(user_input[1]), int(user_input[2]) 
                self.player_board[x][y] = self.FLAG
                self.player_total_spaces -= 1
                self.print_board()
                continue
            elif len(user_input) < 2: 
                print("Wrong input, try again.") 
                continue
            elif user_input[0] == 'test': # for testing purposes 
                eval(user_input[1])
                continue
            elif not user_input[0].isdigit() or not user_input[1].isdigit(): 
                print("Wrong input, try again.") 
                continue
            
            x, y = int(user_input[0]), int(user_input[1])
            if self.real_board[x][y] == self.MINE: 
                print() 
                print("Game over.") 
            else: 
                self.player_board[x][y] = self.real_board[x][y]
                self.player_total_spaces -= 1
                self.print_board() 
            
            if self.player_total_spaces == 0: 
                print() 
                self.print_board()
                print("You win.") 
                return 

    def run_ai(self): 
        self.create_board()
        self.set_board()
        # self.print_board() 

        x, y, res = self.first_move() 
        AI_bot = AI() 
        AI_bot.set_board(self.player_board) 

        while self.real_board[x][y] != self.MINE or self.player_total_spaces > 0: 
            x, y = AI.play_move(x, y, res)
            ...





