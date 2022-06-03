#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:15:04 2018

@author: yangmiao
"""

import tools
import gameai as ai
from checkers import Piece
from checkers import Board
import examples
from string import ascii_lowercase as alphabet
"""
    Write something about this program here.
"""

def indexify(position):
    """
    Write something about this function here.
    """
    first = position[0]
    second = position[1:]
    return (alphabet.index(first), int(second)-1)

def deindexify(row, col):
    """
    Write something about this function here.
    """
    return alphabet[row]+str(col+1)

def initialize(board):
    """
    This function puts white and black pieces according to the checkers
    game positions. The black pieces will be on the top three rows and
    the white pieces will be on the bottom three rows (for an 8x8 board).
    The first row for the black pieces will be placed as a2, a4, a6, ...
    etc. and the next rows will be b1, b3, b5, ... etc. For the white
    rows, the placement patterns will be opposite of those of blacks.
    This must work for any even length board size.
    """
    row = col = board.get_length()
    initrows = (row // 2) - 1
    for r in range(row - 1, row - (initrows + 1), -1):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece('white'))
    for r in range(0, initrows):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece())

def count_pieces(board):
    """
    Write something about this function here.
    """
    black,white = 0,0
    for row in board.get_cells():
        black += sum([1 for piece in row if piece != None and piece.color() == 'black'])
        white += sum([1 for piece in row if piece != None and piece.color() == 'white'])
    return (black,white)

def move_or_capture(board,color,type,is_sorted):
    move = []
    capture = []
    cells = board.get_cells()
    for row,cell in enumerate(cells):
        for col,piece in enumerate(cell):
            if piece != None:
                if piece.color() == color:
                    move += [(deindexify(row,col),p) for p in tools.get_moves(board,row,col,is_sorted)]
                    capture += tools.get_captures(board,row,col,is_sorted)
    if type == 'move':
        return move
    else:
        return capture

def get_all_moves(board, color, is_sorted = False):
    """
    Write something about this function here.
    """
    move_lst = move_or_capture(board,color,'move',is_sorted)
    return sorted(move_lst) if is_sorted else move_lst

def sort_captures(all_captures,is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by the length
    of each sub-list and the sub-lists with the same length will be sorted
    again with respect to the first item in corresponding the sub-list,
    alphabetically.'''
    
    return sorted(all_captures, key = lambda x: (-len(x), x[0])) if is_sorted \
            else all_captures

def get_all_captures(board, color, is_sorted = False):
    """
    Write something about this function here.
    """
    capture_lst = move_or_capture(board,color,'jump',is_sorted)
    return sort_captures(capture_lst,is_sorted)

def apply_move(board, move):
    """
    Write something about this function here.
    
    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function to
            get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.            
    """
    start,end = move
    row1,col1 = indexify(move[0])
    row2,col2 = indexify(move[1])
    l = tools.get_moves(board,row1,col1)
    if l == [] or end not in l:
        raise RuntimeError(move_error)
    else:
        board.place(row2,col2,board.get(row1,col1))
        board.remove(row1,col1)
        if row2 != 0 and row2 != (board.get_length()-1):
            return
        board.get(row2,col2).turn_king()

def apply_capture(board, capture_path):
    """
    Write something about this function here.
    
    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no jump found from any position in capture_path, i.e. use 
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.            
    """
    for i in range(len(capture_path)-1):
        p_f, p_t = capture_path[i:i+2]
        row1,col1 = indexify(p_f)
        row2,col2 = indexify(p_t)
        piece = board.get(row1,col1)
        jumps = tools.get_jumps(board,row1,col1)
        if  jumps == [] or p_t not in jumps:
            raise RuntimeError("Invalid jump/capture, please type" \
                               + " \'hints\' to get suggestions.")
        board.place(row2,col2,board.get(row1,col1))
        board.remove(row1,col1)
        if row2 == 0 or row2 == (board.get_length()-1):
            board.get(row2,col2).turn_king()
        if row2 > row1 and col2 > col1:
            cross = board.get(row2-1,col2-1)
            if cross == None:
                continue
            if cross.color() == board.get(row2,col2).color():
                continue
            board.remove(row2-1,col2-1)
        elif row2 > row1 and col2 < col1:
            cross = board.get(row2-1,col2+1)
            if cross == None:
                continue
            if cross.color() == board.get(row2,col2).color():
                continue
            board.remove(row2-1,col2+1)
        elif row2 < row1 and col2 > col1:
            cross = board.get(row2+1,col2-1)
            if cross == None:
                continue
            if cross.color() == board.get(row2,col2).color():
                continue
            board.remove(row2+1,col2-1)
        elif row2 < row1 and col2 < col1:
            cross = board.get(row2+1,col2+1)
            if cross == None:
                continue
            if cross.color() == board.get(row2,col2).color():
                continue
            board.remove(row2+1,col2+1)


            
def get_hints(board, color, is_sorted = False):
    """
    Write something about this function here.
    """
    capture_lst = get_all_captures(board,color,is_sorted)
    move_lst = get_all_moves(board,color,is_sorted)
    if capture_lst != []:
        move_lst = []
    return (move_lst,capture_lst)
        
def get_winner(board, is_sorted = False):
    """
    Write something about this function here.
    """
    b = get_hints(board,'black',is_sorted)
    w = get_hints(board,'white',is_sorted)
    if b[1] == [] and w[1] != []:
        return 'white'
    if b[1] != [] and w[1] == []:
        return 'black'
    kings = 0
    for row in board.get_cells():
        kings += sum([1 for piece in row if piece and piece.is_king()])
    bc,wc = count_pieces(board)
    if bc + wc == 2:
        if kings == 2:
            return 'draw'
    else:
        if bc > wc:
            return 'black'
        elif bc < wc:
            return 'white'

    return 'draw'

                        
def is_game_finished(board, is_sorted = False):
    """
    Write something about this function here.
    """
    b = get_hints(board,'black',is_sorted)
    w = get_hints(board,'white',is_sorted)
    if (b[1] != [] or b[0] != []) and (w[1] != [] or w[0] !=[]):
        return False
    return True

# Some error messages to save lines.
move_error = "Invalid move, please type \'hints\' to get suggestions."
hasjump_error = "You have jumps, please type \'hints\' to get suggestions."
jump_error = "Invalid jump, please type \'hints\' to get suggestions."
hint_error = "Invalid hint number."
cmd_error = "Invalid command."

def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    """    
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    
    prompt = "[{:s}'s turn] :> "
    print(tools.banner)
   
    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()
    
    # Take a board of size 8x8
    board = Board(8)
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()
            
            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}"\
                                  .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play human ---
    
def game_play_ai():
    """
    This is the main mechanism of the human vs. ai game play. You need to
    implement this function by taking helps from the game_play_human() 
    function.
    
    For a given board situation/state, you can call the ai function to get
    the next best move, like this:
        
        move = ai.get_next_move(board, turn)
        
    where the turn variable is a color 'black' or 'white', also you need to 
    import ai module as 'import gameai as ai' at the beginning of the file.
    This function will be very similar to game_play_human().
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    
    prompt = "[{:s}'s turn] :> "
    print(tools.banner)
    
    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()
    
    # Take a board of size 8x8
    board = Board(8)
    initialize(board)
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            print("Current board:")
            board.display(piece_count)
            #opponet's turn
            if turn == opponent_color:
                move = ai.get_next_move(board, turn)
                print("\t{:s} played {:s}.".format(turn, str(move)))
                p_f, p_t = move[0:2]
                row1,col1 = indexify(p_f)
                row2,col2 = indexify(p_t)
                if abs((row1) - int(row2)) == 2:
                    apply_capture(board,move)
                else:
                    apply_move(board,move)
                turn = my_color
            else:
                # Get the command from user using input
                command = input(prompt.format(turn)).strip().lower()
                
                # Now decide on different commands
                if command == 'pass':
                    break
                elif command == 'exit':
                    break
                elif command == 'hints':
                    (moves, captures) = get_hints(board, turn, True)
                    if moves:
                        print("You have moves:")
                        for i, move in enumerate(moves):
                            print("\t{:d}: {:s} --> {:s}"\
                                  .format(i + 1, move[0], move[1]))
                    if captures:
                        print("You have captures:")
                        for i, path in enumerate(captures):
                            print("\t{:d}: {:s}".format(i + 1, str(path)))
                else:
                    command = [s.strip().lower() for s in command.split()]
                    (moves, captures) = get_hints(board, turn, True)
                    action = None
                    if command and command[0] == 'move' and len(command) == 3:
                        if not captures:
                            action = (command[1], command[2])
                            if action in moves:
                                apply_move(board, action)
                            else:
                                raise RuntimeError(move_error)
                        else:
                            raise RuntimeError(hasjump_error)
                    elif command and command[0] == 'jump' and len(command) >= 3:
                        action = command[1:]
                        if action in captures:
                            apply_capture(board, action)
                        else:
                            raise RuntimeError(jump_error)
                    elif command and command[0] == 'apply' and len(command) == 2:
                        id_hint = int(command[1])
                        if moves and (1 <= id_hint <= len(moves)):
                            action = moves[id_hint - 1]
                            apply_move(board, action)
                        elif captures and (1 <= id_hint <= len(captures)):
                            action = captures[id_hint - 1]
                            apply_capture(board, action)
                        else:
                            raise ValueError(hint_error)
                    else:
                        raise RuntimeError(cmd_error + tools.usage)
                    print("\t{:s} played {:s}.".format(turn, str(action)))
                    turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play ai ---

def main():
    game_play_ai()


# main function, the program's entry point
if __name__ == "__main__":
    main()
