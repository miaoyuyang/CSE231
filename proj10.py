###############################################################################
#   Project 10
#
# In this project, there will be a game -- ‘CHECKERS’, in which human players 
#  will compete with computer players. First, I use from 'string import ascii_
#   lowercase as alphabet' to transfer alphabet to row-column. The column start
#    from 1. The next func, it's the opposite of the previous one, it will be
#     return a tuple. Then, The purpose of count_pieces() is to count the total
#      number of pieces on the current board. It returns a tuple with the num
#       of black pieces in front. The ways of get_all_moves() and get_all_capt
#        ures is similar. They need to use tool to catch the postion and return
#         a list. Also, the way of apply_move() is similar to apply_capture().
#          I use for loop to find capture and moved, and use if-elif-else to 
#           check out them. In the function of get_hints(), it will return the
#            tuple, if the first list have datas, it exit jumps. In the func of
#             get_winner(), I use if to check four possible results, and return
#              the winner. In the func of is_game_finished(), it will get datas
#               from get_hints(), and use if loop to check the result, and 
#                return True or False. Due to the game_play_human() is provided
#                 so, in the game_play_ai(), I just need to add 16 lines.
############################################################################### 
import tools
import gameai as ai
from checkers import Piece
from checkers import Board
from string import ascii_lowercase as alphabet

def indexify(position):
    """
    This function converts an alphanumeric position to a row-column index. 
    I will use 'from string import ascii_lowercase as alphabet'.
    And this function will return the tuple.
    """
    row = alphabet.index(position[0]) # a to z
    column = int(position[1:])-1 # starting from 1
    return row, column # return the postion

def deindexify(row, col):
    """
    This function converts a row-column index to an alphanumeric position.
    And this function will return the string.
    """
    value_row = alphabet[row]  # the number of row
    value_column = str(col + 1) # the number of column
    return value_row + value_column 

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
    This function is to calculate the total numeber on the board currently.
    I use if loop, if the color is black the count will be add one.
    And it will return the tuple, which black count will be first.
    """
    value_black = 0 #count
    value_white = 0
    for row in range(board.get_length()): # get the row
        for column in range(board.get_length()): # get the column
            piece = board.get(row,column) 
            if piece != None: # if have pieces on this board.
                if piece.color() == 'black': # if the piece's color is black
                    value_black +=1 #the count of black add one
                elif piece.color() == 'white': # if the piece's color is white
                    value_white +=1 #the count of white add one
                    
    return value_black,value_white # the count of black will come first 
                
def get_all_moves(board, color, is_sorted = False):
    '''
    The purpose of this function is to find the positions of all moved pieces, 
    which are returned as a list of tuples. I will use for loop to got them.
    '''
    moves = [] # creat a list
    for row in range(board.get_length()): #get the row  
        for column in range(board.get_length()):#get the col
            piece = board.get(row,column)
            if piece != None:
                if piece.color() == color:
                    move = tools.get_moves(board,row,column,is_sorted)
                    for i in move:
                        moves.append((deindexify(row,column),i)) #combain to tup
                        
    if is_sorted == True:
        return sorted(moves) #sort them
    else:
        return moves
   
def sort_captures(all_captures,is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by the length
    of each sub-list and the sub-lists with the same length will be sorted
    again with respect to the first item in corresponding the sub-list,
    alphabetically.'''
    
    return sorted(all_captures, key = lambda x: (-len(x), x[0])) if is_sorted \
            else all_captures

def get_all_captures(board, color, is_sorted = False):
    """
    This function is used to locate all captured pieces and returns a list.
    if the postion of piece exit, I will use tools to find them. And add them 
    into the list.
    """
    capture = [] # creat a list
    for row in range(board.get_length()): # get the row
        for column in range(board.get_length()): # get the column
            piece = board.get(row,column)
            if piece != None: # if have pieces on the board
                if piece.color() == color:
                    capture += tools.get_captures(board,row,column,is_sorted)
                    # add the postion into the list
    if is_sorted == True:
        return sort_captures(capture, is_sorted) 
    else:
        return capture
            
def apply_move(board, move):
    """
    This function describes the two positions in which a piece is moved.
    If the board don't have movement or the second postion not in movement,
    it will raise RuntimeError.
    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function to
            get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.            
    """

    start,over = move # remove two pieces
    r1,c1 = indexify(move[0]) # The starting position of a piece
    r2,c2 = indexify(move[1]) # The ending position of a piece
    movement = tools.get_moves(board,r1,c1) 
    if movement == [] or movement[-1] not in movement:#check validity moves
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.") 
    else:
        choose_piece = board.get(r1,c1)
        board.place(r2,c2,choose_piece)
        board.remove(r1,c1) # remove the first piece
        if choose_piece.color() == 'white': # if the color is white
            if r2 == 0:
                return choose_piece.turn_king() 
        elif choose_piece.color() == 'black': # if the color is black
            if r2 ==(board.get_length()-1):
                return choose_piece.turn_king() # become the king piece

def apply_capture(board, capture_path):
    """
    This function is find a capture on the board. If don't have jumps or if its
    a vaild jump, it will show the Error information. I will use tools.py to 
    find them.
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
        ex_r,ex_c = capture_path[i:i+2] 
        r1,c1 = indexify(ex_r)
        r2,c2 = indexify(ex_c)
        jump = tools.get_jumps(board,r1,c1) # use tools.py to find them
        if jump == [] or ex_c not in jump: # if the jump is invalid
            raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.") 
        else:
            choose_capture = board.get(r1,c1)
            board.place(r2,c2,choose_capture)
            prey_r = int((r1+r2)/2) # the center postion about row
            prey_c = int((c1+c2)/2) # the center postion about column
            board.remove(prey_r,prey_c) # remove the center pieces
            board.remove(r1,c1) 
            if choose_capture.color() == 'white': # check whie pieces
                if r2 ==0:
                    choose_capture.turn_king() # become king pieces
            elif choose_capture.color() == 'black': # check black pieces
                if r2==(board.get_length()-1):
                    choose_capture.turn_king()
        
def get_hints(board, color, is_sorted = False):
    """
    The purpose of this function is provide the player a hint about valid moves
    it will return the tuple.
    """
    data_cap = get_all_captures(board, color, is_sorted)
    data_move = get_all_moves(board, color, is_sorted)
    
    if data_cap != []: # if the first list have datas, it exit jumps.
        data_move = []
    return data_move,data_cap # return tuple
        
def get_winner(board, is_sorted = False):
    """
    The purpose of this function is to find winner. I will get the data from
    get_hints(), and use if loop to check who's the winner. And this function
    will return 'black', 'white' or 'draw'.
    """

    black_player = get_hints(board, 'black', is_sorted)
    white_player = get_hints(board, 'white', is_sorted)
    count_kings = 0 # setup a kings count
    count_black, count_white = count_pieces(board) # got the total number
    for row in board.get_cells():
        count_kings += sum([1 for piece in row \
                            if piece and piece.is_king()])
    # if only black still has moves or captures, the winner is black
    if (black_player[0]==[] or black_player[1]==[])and \
    not (white_player[0]==[] or white_player[1]==[]):
        return 'black' # the winner is black
    # if only white still has moves or captures, the winner is white
    if (white_player[0]==[] or white_player[1]==[])and \
    not (black_player[0]==[] or black_player[1]==[]):
        return 'white'
    # If there is one white king and one black king left on the board 
    if (count_black == count_white ==1) and (count_kings ==2):
        return 'draw'
    # If there is one white piece and one black piece left on the board 
    if count_black == count_white ==1:
        return 'draw'
    else:
        # if the number of black piece more than white pices, the winner is black
        if count_black > count_white:
            return 'black'
        #if the number of black piece less than white pices, the winner is black
        if count_black < count_white:
            return 'white'
    
def is_game_finished(board, is_sorted = False):
    """
    The purpose of this function is to check if the game finished. I will use
    if loop to check them and return True or False.
    """
    # call the function of get_hints() to get datas.
    black_player = get_hints(board, 'black', is_sorted)
    white_player = get_hints(board, 'white', is_sorted)
    # If neither black nor white player has zero pieces, it will return False.
    if (black_player[0] != [] or black_player[1] != []) and \
    (white_player[0] != [] or white_player[1] != []):
        return False
    # Otherwise, it will return True.
    else:
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
    # Piece.symbols = ['b', 'w']
    # Piece.symbols_king = ['B', 'W']
    
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
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    Piece.symbols = ['b', 'w'] # the normal pieces
    Piece.symbols_king = ['B', 'W'] # use upper to show the piece become king
    
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
         
            if turn == opponent_color:
                action = ai.get_next_move(board, turn)           
                ex_1, ex_2 = action[0:2]
                r1,c1 = indexify(ex_1)
                r2,c2 = indexify(ex_2)
                if r1 - r2 == 2:
                    apply_capture(board, action)
                elif r2 - r1 == 2:
                    apply_capture(board, action)   
                else:
                    apply_move(board, action)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
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
    
    game_play_human()

# main function, the program's entry point
if __name__ == "__main__":
    main()
