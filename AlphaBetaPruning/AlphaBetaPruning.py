# CS 143 Artificial Intelligence Assignment \#6
# author: Blake Gerold
# proposed points: 18 (out of 20)  -- not changing this line automatically results a 1 point deduction

# 8/8 minimax: I got this to work along with a "simple" utility function. Blocks player if they are about to win

# 4/4 depth paramter: I added this to the minimax function that returns the utility after the AI's minimax makes
#                     so many predictions ahead

# 4/4 alpha-beta prunning: Alpha-beta pruning works and I am able to prove this by running the plain minimax alongside
#                          the alpha-beta version. Alphas-beta has much faster running times.

# 3/4 sophisticate utitlity: This utitlity works somewhat! It still blocks the player and goes into positions other than 0
#     when adding pieces, but it still makes dumb mistakes but rarely.


# comments: Special thanks to Keith Galli for supplying the foundation for the Connect 4 code
#           https://github.com/KeithGalli/Connect4-Python

import math
import time

NUMBER_OF_ROWS = 6
NUMBER_OF_COLS = 7

HUMAN_PLAYER = 'x'
AI_PLAYER = 'o'

class ConnectFourGame :

    def __init__(self):
        # initialize the starting board
        self.initial = [['.'] * NUMBER_OF_COLS for _ in range(NUMBER_OF_ROWS)]

    def display(self, state):
        """Print or otherwise display the state."""
        print()
        for row in range(NUMBER_OF_ROWS-1,-1,-1):
            print("|\t",end='')
            for col in range(NUMBER_OF_COLS):
                print(state[row][col],"\t", end="")
            print("|")

        print("-" * 66)
        bk = "   |   "
        print(" "*8+"0"+bk+"1"+bk+"2"+bk+"3"+bk+"4"+bk+"5"+bk+"6") 


    def is_valid_location(self, state, col):
        if col <0 or col >= NUMBER_OF_COLS:
            return False
        else:
            return state[NUMBER_OF_ROWS - 1][col] == '.'

    def get_next_open_row(self, state, col):
        for r in range(NUMBER_OF_ROWS):
            if state[r][col] == '.':
                return r
        return NUMBER_OF_ROWS

    def winning_state(self, state, piece):
        # Check horizontal locations for win
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS):
                if state[r][c] == piece and state[r][c+1] == piece and state[r][c+2] == piece and state[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(NUMBER_OF_COLS):
            for r in range(NUMBER_OF_ROWS - 3):
                if state[r][c] == piece and state[r+1][c] == piece and state[r+2][c] == piece and state[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS - 3):
                if state[r][c] == piece and state[r+1][c+1] == piece and state[r+2][c+2] == piece and state[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(3, NUMBER_OF_ROWS):
                if state[r][c] == piece and state[r-1][c+1] == piece and state[r-2][c+2] == piece and state[r-3][c+3] == piece:
                    return True
        return False

    def terminal_test(self, state):
        return self.winning_state(state, "x") or self.winning_state(state, "o") or len(self.actions(state)) == 0


    def actions(self, state):
        # returns list of numbers corresponding to possible moves
        valid_locations = []
        for col in range(NUMBER_OF_COLS):
            if self.is_valid_location(state, col):
                valid_locations.append(col)
        return valid_locations

    def result(self, state, move, player):
        """Return the state that results from making a move from a state."""
        row = self.get_next_open_row(state, move)
        state[row][move] = player
        return state

    def undo(self, state, move):
        """Undo a given move. return the state"""
        row = self.get_next_open_row(state, move)
        state[row-1][move] = '.'
        return state

    def getEnemyPlayer(self, player):
        # return the opposite of player
        if player == 'x':
            return 'o'
        else:
            return 'x'

#     def utility(self, state, player, move): #simple utility
#         """Return the value of this final state to player."""
#         if self.winning_state(state, 'o'):
#             return 1
#         
#         elif self.winning_state(state, 'x'):
#             return -1
#         
#         else:
#             return 0
        
    def utility(self, state, player, move):
        """Return the value of this state for the player."""
        #print(move)
        
        if self.winning_state(state, 'o'):
            return 5
        
        elif self.winning_state(state, 'x'):
            return -5
        
        else:
            if move == 3:
                #print("Returning INT 3")
                return 4
            if move == 2:
                #print("Returning INT 2")
                return 3
            if move == 4:
                #print("Returning INT ")
                return 3
            if move == 1:
                #print("Returning INT")
                return 2
            if move == 5:
                #print("Returning INT")
                return 2
            if move == 0:
                #print("Returning INT")
                return 1
            if move == 6:
                #print("Returning INT")
                return 1

    def minimax(self, state, player, depth, alpha, beta, move):
        
        if depth == 0 or self.terminal_test(state):
            return self.utility(state, player, move), None
        
        if player == 'o': #maximizing player
            best = -math.inf
            move = 0
            for move in self.actions(state):
                state = self.result(state, move, player)
                val, _ = self.minimax(state, self.getEnemyPlayer(player), depth -1, alpha, beta, move)
                #print("max", val)
                
                #print("player", player, "move",move,"val",val)
                
                #undo the move
                state = self.undo(state, move)
                
                if val > best :
                    best, bestMove = val, move
                
                if best > alpha:
                    alpha = best
                    
                if beta <= alpha:
                    break

        else: #minimizing player
            best = math.inf
            move = 0
            for move in self.actions(state):
                state = self.result(state, move, player)
                
                val, _ = self.minimax(state, self.getEnemyPlayer(player), depth -1, alpha, beta, move)
                #print("player", player, "move",move,"val",val)
                #print("Min", val)
                # undo the move
                state = self.undo(state, move)
                
                if val < best :
                    best, bestMove = val, move
                
                if best < beta:
                    beta = best
                
                if beta <= alpha:
                    break

        return best, bestMove

    def minimaxPLAIN(self, state, player, depth, move):
        
        if depth == 0 or self.terminal_test(state):
            return self.utility(state, player, move), None

        if player == 'x': #maximizing player
            best = -math.inf
            for move in self.actions(state):
                state = self.result(state, move, player)
                val, _ = self.minimaxPLAIN(state, self.getEnemyPlayer(player), depth -1, move)
                
                
                # undo the move
                #state = self.result(state, move, '.')
                state = self.undo(state, move)
                

                if val > best :
                    best, bestMove = val, move

        else: #minimizing player
            best = math.inf
            for move in self.actions(state):
                #print(move)
                state = self.result(state, move, player)
                val, _ = self.minimaxPLAIN(state, self.getEnemyPlayer(player), depth -1, move)
                
                # undo the move
                #state = self.result(state, move, '.')
                state = self.undo(state, move)

                if val < best :
                    best, bestMove = val, move
            #print (best, bestMove)
            
        return best, bestMove

    def play(self, state):
        """" play a game of connect 4 """
        game_over = False
        turn = 1
        while not game_over:
            self.display(state)
            if turn == 1:
                print("PLAYER 1")
                col = int(input("Where to drop a piece? "))
                if self.is_valid_location(state, col):
                    state = self.result(state, col, 'x')
                    turn = 2
                else:
                    print('not a valid location; try again')

                if self.winning_state(state, 'x'):
                    print("Player 1 wins!")
                    game_over = True

            else:
                print("AI")
                startTime = time.time()
                val, col = game.minimax(state, 'o', 7, -math.inf, math.inf, 0) 
                print("Value: ",val)
                print("Minmax Alpha-Beta Prunimg Run Time:", time.time() - startTime)
                #print("Found minimax")
                
                startTime = time.time()
                game.minimaxPLAIN(state, "o", 7, None)
                print("Minmax PLAIN Run Time:", time.time() - startTime)
                
#                 if val == 4:
#                     col = 3
#                     
#                 if val == 3:
#                     x = (2,4)
#                     col = random.choice(x)
#                     
#                 if val == 2:
#                     x = (1,5)
#                     col = random.choice(x)
#                     
#                 if val == 1:
#                     x = (0,6)
#                     col = random.choice(x)

                if self.is_valid_location(state, col):
                    state = self.result(state, col, 'o')
                    turn = 1
                else:
                    print('not a vaild location; try again')

                if self.winning_state(state, 'o'):
                    print("AI wins!")
                    game_over = True

        self.display(state)

#play the game
game = ConnectFourGame()
game.play(game.initial)