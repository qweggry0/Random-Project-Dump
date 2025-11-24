import random, time
import math


class GameBoard:
    def __init__(self):
        # test list: 
        #self.board_state = [' ', ' ', 'O', ' ', 'O', ' ', 'O', ' ', ' ']
        self.board_state = self.GenerateBoard()      


    def GenerateBoard(self):
        psudo_board = [" " for i in range(9)] 
        return psudo_board


    def print_board(self, b):
        for i in range(0, 9, 3):
            print("|" + b[i] + "|" + b[i+1] + "|" + b[i+2] + "|")
    

    def AvailableMoves(self):
        a_moves = []
        for i in range(len(self.board_state)):
            if self.board_state[i] not in ["X", "O"]:
                a_moves.append(i)
            else:
                pass
        if len(a_moves) == 0:
            return 0
        else:
            return a_moves
    

    def Move(self, letter, index):
        self.board_state[index] = letter


    def WinCondition(self, p1_symbol, bot_symbol):
        count = 0

        # win conditions for rows
        for y in range(3):
            psudo_list = []
            for x in range(3):
                psudo_list.append(self.board_state[count])
                count += 1

            if psudo_list.count(p1_symbol) == len(psudo_list) or psudo_list.count(bot_symbol) == len(psudo_list):
                return psudo_list[0]
        
        # win conditions for columns:
        for y in range(3):
            psudo_list = []
            for x in range(3):
                psudo_list.append(self.board_state[y+3*x])
            if psudo_list.count(p1_symbol) == len(psudo_list) or psudo_list.count(bot_symbol) == len(psudo_list):
                return psudo_list[0]
        
        # win conditions for Diagonals
        count = 0
        psudo_list = []
        for i in range(3): # first diagonal
            psudo_list.append(self.board_state[count])
            count += 4
        if psudo_list.count(p1_symbol) == len(psudo_list) or psudo_list.count(bot_symbol) == len(psudo_list):
                return psudo_list[0]

        count = 2
        psudo_list = []
        for i in range(3): # second diagonal
            psudo_list.append(self.board_state[count])
            count += 2
        if psudo_list.count(p1_symbol) == len(psudo_list) or psudo_list.count(bot_symbol) == len(psudo_list):
            return psudo_list[0]
        
        if self.AvailableMoves() == 0:
            return 0
        return None



class Player: 
    def __init__(self, symbol):
        self.symbol = symbol
        self.turn = True

class Bot:
    def __init__(self, symbol):
        self.symbol = symbol
        self.turn = False



    


class TicTacToe():
    def __init__(self):
        self.board = GameBoard()
        self.p1 = Player("X")
        self.b1 = Bot("O")
        self.attempts = 0
        self.MainGameLoop()
    
    def MainGameLoop(self):
        run = True

        while run == True:
            # Check for win
            win = self.board.WinCondition(self.p1.symbol, self.b1.symbol)
            if win != None:
                self.board.print_board(self.board.board_state)

            if win == self.p1.symbol:
                print("PLAYER WINS")
                run = False
                break
            elif win == self.b1.symbol:
                print("Bot wins")
                run = False
                break
            elif win == 0:
                print("draw")
                run = False
                break
            else:
                pass
            
            self.board.print_board(self.board.board_state)
            available_moves = self.board.AvailableMoves()
            
            # Movements are played here
            if self.p1.turn == True:
                print("Player 1 turn:")
                self.MakeMove(self.p1.symbol, available_moves)
                self.p1.turn = False
                self.b1.turn = True
            elif self.b1.turn == True:
                print("Bot turn:")
                self.board.Move(self.b1.symbol, self.BotMove(self.b1.symbol, available_moves))
                self.p1.turn = True
                self.b1.turn = False
            else:
                print("ERROR")

            self.attempts += 1


    def MakeMove(self, letter, moves):
        # Validity check
        index = input(f"Enter which index: ")
        try:
            index = int(index)
        except:
            print("Integers are only accepted, retrying...\n")
            self.MainGameLoop()
        
        index -= 1

        if index < 0 or index > 8:
            print("Index out of range, retrying...\n")
            self.MainGameLoop()

        if index not in moves:
            print("Invalid movement, retrying...\n")
            self.MainGameLoop()
        self.board.Move(letter, index)
    

    def MiniMax(self, depth, is_maximising, symbol, curr_board, p_moves):
        # WIN CONDITION, iteration stops here if conditions are met
        let = self.board.WinCondition(self.p1.symbol, self.b1.symbol)
        if let == self.b1.symbol: # maximising
            return 10 - depth # using 10 as tic tac toe only has 9 possible moves
        elif let == self.p1.symbol: # minimising
            return depth - 10
        elif let == 0: # Draw
            return 0
        
        # ITERATIONS
        if is_maximising == True: # maximising
            best_score = -float('inf')
            best_move = None
            for move in p_moves:
                self.board.Move(self.b1.symbol, move)
                next_moves = self.board.AvailableMoves()
                # iterates through all possible moves from this branch
                score = self.MiniMax(depth + 1, False, self.b1.symbol, self.board.board_state, next_moves)
                self.board.Move(" ", move)
                best_score = max(score, best_score)
            return best_score
        else: # Minimising
            best_score = float('inf')
            for move in p_moves:
                self.board.Move(self.p1.symbol, move)
                next_moves = self.board.AvailableMoves()
                score = self.MiniMax(depth + 1, True, self.p1.symbol, self.board.board_state, next_moves)
                self.board.Move(" ", move)
                best_score = min(score, best_score)
            return best_score


                
    
    def BotMove(self, letter, a_moves):
        # Random attempt for only 1 move (optimisation)
        if self.attempts <= 1:
            return random.choice(a_moves)
        best_score = -float("inf")

        # goes through all possible branches from terminal state
        for move in a_moves:
            self.board.Move(self.b1.symbol, move) 
            next_moves = self.board.AvailableMoves()

            # runs minmax for this branch
            score = self.MiniMax(0, False, self.b1.symbol, self.board.board_state, next_moves)

            # undoing move
            self.board.Move(" ", move)  
            if score > best_score:  # store best move
                best_score = score
                best_move = move

        return best_move

        
            

            
        

            




if __name__ == "__main__":
    root = TicTacToe()      