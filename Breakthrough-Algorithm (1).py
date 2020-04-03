#!/usr/bin/env python
# coding: utf-8

# In[816]:


'''
Representation of state will keep track of white and black piece locations, as well as the size of the board. 
Our group believes just these parameters will be able to keep track of any given board position/state. 
Each position will be stored as a letter followed by a number combination with letters 
correlating to rows and numbers correlating to columns. 
Position a1 will be the top left of the board, the string X will represent white pieces that will start 
on the top of the board, and O will represent the black pieces starting on the bottom of the board.
'''


#for this lab, X is for WHITE PIECES and WHITE PIECES start on TOP OF BOARD

import copy
class Breakthrough:
        def __init__(self, num_rows, num_columns, num_rows_pieces):
            self.num_rows = num_rows
            self.num_columns = num_columns
            self.num_rows_pieces = num_rows_pieces            
            
        def write_initial_state(self):
            rows = 'abcdefghi'
            columns = '123456789'
            white = []
            black = []
            for row in range (self.num_rows_pieces): 
                for column in range (self.num_columns): 
                    white.append(rows[row]+columns[column]) 
            cut_rows = ''

            for row in range (self.num_rows):
                cut_rows += rows[row]

            fixed_cut_rows = cut_rows[::-1]
            for row in range (self.num_rows_pieces):
                for column in range (self.num_columns):
                    black.append(fixed_cut_rows[row]+columns[column])
            
            return [white, black, self.num_rows, self.num_columns, 'W']
            
        
        def display_current_state(self, state):
            white = state[0]
            black = state[1]
            rows = 'abcdefghi'
            columns = '123456789'
            current_state = ''
            for row in range (self.num_rows):
                current_state += "\n"
                for column in range (self.num_columns):
                    if (rows[row]+columns[column]) in white:
                        current_state += 'X'
                    elif (rows[row]+columns[column]) in black:
                        current_state += 'O'
                    else:
                        current_state += '.'

            print (current_state)           
            
    
        def display_state(self, white, black):
            rows = 'abcdefghi'
            columns = '123456789'
            current_state = ''
            for row in range (self.num_rows):
                current_state += "\n"
                for column in range (self.num_columns):
                    if (rows[row]+columns[column]) in white:
                        current_state += 'X'
                    elif (rows[row]+columns[column]) in black:
                        current_state += 'O'
                    else:
                        current_state += '.'

            return current_state
        
 
        def initial_state(self):
            rows = 'abcdefghi'
            columns = '123456789'
            white = []
            black = []
            for row in range (self.num_rows_pieces): 
                for column in range (self.num_columns): 
                    white.append(rows[row]+columns[column]) 
            cut_rows = ''

            for row in range (self.num_rows):
                cut_rows += rows[row]

            fixed_cut_rows = cut_rows[::-1]
            for row in range (self.num_rows_pieces):
                for column in range (self.num_columns):
                    black.append(fixed_cut_rows[row]+columns[column])

            return self.display_state (white, black)


#state will be represented as state = [white, black, num_rows, num_columns, player_turn]
#move will be represented as move = [current_location, to_move_location]
#we will use this function so will make sure move is valid move beforehand

def transition(state, move):
    white = copy.deepcopy(state[0])
    black = copy.deepcopy(state[1])
    num_rows = copy.deepcopy(state[2])
    num_columns = copy.deepcopy(state[3])
    player_turn = copy.deepcopy(state[4])
    current_location = copy.deepcopy(move[0])
    to_move_location = copy.deepcopy(move[1])


    if player_turn == 'W':
        if current_location in white:
            white.remove(current_location)
            white.append(to_move_location)
        if to_move_location in black:
            black.remove(to_move_location)
        player_turn = 'B'

    elif player_turn == 'B':
        if current_location in black:
            black.remove(current_location)
            black.append(to_move_location)
        if to_move_location in white:
            white.remove(to_move_location)
        player_turn = 'W'

    return [white, black, num_rows, num_columns, player_turn] #returning a new state
    
    
    
def terminal_test(state):
    rows = 'abcdefghi'
    num_rows = state[2]
    white = state[0]
    black = state[1]
    if any(rows[num_rows-1] in s for s in white):
        return True
    if any(rows[0] in s for s in black):
        return True
    if white == []:
        return True
    if black == []:
        return True
    return False


def move_generator(state):
    rows = 'abcdefghi'
    columns = '123456789'

    player_turn = state[4]
    white = state[0]
    black = state[1]
    possible_moves = []
    if player_turn == 'W':
        for pos in white:
            current_pos = pos
        
            row_index = rows.index(current_pos[0])
           
            column_index = columns.index(current_pos[1])
            row_index += 1
            for possible in range (3):

                if possible == 0:
                    if not rows[row_index]+columns[column_index-1] in white and current_pos[1] != columns[0]:
                        possible_moves.append([current_pos, rows[row_index]+columns[column_index-1]])

                if possible == 1:
                    if not rows[row_index]+current_pos[1] in black and not rows[row_index]+current_pos[1] in white:
                        possible_moves.append([current_pos, rows[row_index]+current_pos[1]])

                if possible == 2:
                    if not rows[row_index]+columns[column_index+1] in white and current_pos[1] != columns[state[3]-1]:
                        possible_moves.append([current_pos, rows[row_index]+columns[column_index+1]])

    if player_turn == 'B':
        for pos in black:
            current_pos = pos
            row_index = rows.index(current_pos[0])
            column_index = columns.index(current_pos[1])
            row_index -= 1
            for possible in range (3):

                if possible == 0:
                    if not rows[row_index]+columns[column_index-1] in black and current_pos[1] != columns[0]:
                        possible_moves.append([current_pos, rows[row_index]+columns[column_index-1]])

                if possible == 1:
                    if not rows[row_index]+current_pos[1] in black and not rows[row_index]+current_pos[1] in white:
                        possible_moves.append([current_pos, rows[row_index]+current_pos[1]])

                if possible == 2:
                    if not rows[row_index]+columns[column_index+1] in black and current_pos[1] != columns[state[3]-1]:
                        possible_moves.append([current_pos, rows[row_index]+columns[column_index+1]])


    return possible_moves


# In[817]:


import copy
def minimax(heuristic, state, depth, max_player):
    if depth == 0 or terminal_test(state) == True:
        return [heuristic(state), None]
    if max_player:
        max_val_move = [float("-inf"), None]
        for move in move_generator(state):
            valued_move = [None, None]
            valued_move[0] = minimax(heuristic, copy.deepcopy(transition(state, move)), depth-1, False)[0]
            valued_move[1] = move
         
            if valued_move[0] >= max_val_move[0]:
                max_val_move = valued_move
            
        return max_val_move
    
    else:
        min_val_move = [float("inf"), None]
        for move in move_generator(state):
            valued_move = [None, None]
            valued_move[0] = minimax(heuristic, copy.deepcopy(transition(state, move)), depth-1, True)[0]
            valued_move[1] = move
            if valued_move[0] <= min_val_move[0]:
                min_val_move = valued_move
        return min_val_move
    
    
board = Breakthrough(3,3,1)
state = board.write_initial_state()
print(minimax(ai_michael, state, 5, True))


# In[855]:


#utility functions
#state = [white, black, num_rows, num_columns, player_turn]
import random

def evasive (state):
    player = state[4]
    if player == 'W':
        return (len(state[0]) + random.uniform(0, 1))
    if player == 'B':
        return (len(state[1]) + random.uniform(0, 1))

def conqueror (state):
    player = state[4]
    if player == 'W':
        return (0-len(state[1]) + random.uniform(0, 1))
    if player == 'B':
        return (0-len(state[0]) + random.uniform(0, 1))

#several attempts (still needs improvement)
def gogo_forward (state):
    rows = 'abcdefghi'
    player = state[4]
    value = 0
    if player == 'B':
        for piece in state[0]:
            if rows.index(piece[0]) == state[2]-1:
                return (+100000)
            if rows.index(piece[0]) <= value:
                value = rows.index(piece[0])
        return (-value + random.uniform(0,1))
            
    if player == 'W':
        for piece in state [1]:
            if rows.index(piece[0]) == 0:
                return (-100000)
            if rows.index(piece[0]) <= value:
                value = rows.index(piece[0])
        return (value + random.uniform(0,1))

def ai_michael (state):
    rows = 'abcdefghi'
    player = state[4]
    value = 0
    if player == 'B':
        for piece in state[0]:
            if rows.index(piece[0]) == state[2]-1:
                return (100000 + random.uniform(0,1))
        for piece in state[1]:
            if rows.index(piece[0]) == 0:
                return (-100000 + random.uniform(0,1))
        for piece in state[0]:
            if rows.index(piece[0]) <= value:
                value = rows.index(piece[0])
        return (-value + random.uniform(0,1))
    if player == 'W':
        for piece in state[0]:
            if rows.index(piece[0]) == state[2]-1:
                return (-100000 + random.uniform(0,1))
        for piece in state[1]:
            if rows.index(piece[0]) == 0:
                return (100000 + random.uniform(0,1))
        for piece in state [1]:
            if rows.index(piece[0]) >= value:
                value = rows.index(piece[0])
        return (value + random.uniform(0,1))
    
def evading_conqueror (state):
    player = state[4]
    if player == 'W':
        return(len(state[0])-len(state[1]) + random.uniform(0,1))
    if player == 'B':
        return(len(state[1])-len(state[0]) + random.uniform(0,1))


# In[861]:


#board_state = [num_rows, num_columns, num_rows_pieces]
def play_game (heuristic_white, heuristic_black, board_state):
    num_rows = board_state[0]
    num_columns = board_state[1]
    num_rows_pieces = board_state[2]
    board = Breakthrough(num_rows, num_columns, num_rows_pieces)
    initial_state = board.write_initial_state()
    current_state = board.write_initial_state()
    move_counter = 0
    player_turn = current_state[4]
    move = [None, None]
    
    while terminal_test(current_state) == False:
        if player_turn == 'W':
            move = minimax(heuristic_white, current_state, 3, True)[1]
            current_state = transition(current_state, move)
        else:
            move = minimax(heuristic_black, current_state, 3, True)[1]
            current_state = transition(current_state, move)

        move_counter += 1
        #board.display_current_state(current_state)

    white_has_taken = len(initial_state[1])-len(current_state[1])
    black_has_taken = len(initial_state[0])-len(current_state[0])
    
    if move_counter%2 != 0:
        print('White has won in', move_counter//2+1, 'moves! \nIn the process, White has taken', white_has_taken, 'Black pieces!')
    else:
        print('Black has won in', move_counter//2, 'moves! \nIn the process, Black has taken', black_has_taken, 'White pieces!')

