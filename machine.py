win_ways = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]


def get_position_to_win(board):
    '''Returns the position to win the game.
       In a 3x3 board, it will return values from 0 to 8 
    '''
    for way in win_ways:
        machine_count = 0
        free_count = 0
        position_to_win = None
        for pos in way:
            x = pos//3
            y = pos % 3
            position = board[x][y]
            if position == 2:
                machine_count += 1
            elif position == 0:
                free_count += 1
                position_to_win = pos
            if machine_count == 2 and free_count == 1:
                return position_to_win
    return None

def get_position_to_block (board):
    '''
        Returns the position to block the opponent
        In a 3x3 board, it will return values from 0 to 8 
    '''
    for way in win_ways:
        user_count = 0
        free_count = 0
        position_to_block = None
        for pos in way:
            x = pos//3
            y = pos % 3
            position = board[x][y]
            if position == 1:
                user_count += 1
            elif position == 0:
                free_count += 1
                position_to_block = pos
            if user_count == 2 and free_count == 1:
                return position_to_block
    return None

def get_position_to_play(board):
    '''Returns a random position to play.
       If a "way to win" is availabe, returns a position of it'''
    for way in win_ways:
        user_count = 0
        free_count = 0
        position_to_play = None
        positions_checked = 0
        for pos in way:
            x = pos//3
            y = pos % 3
            position = board[x][y]
            positions_checked +=1
            if position == 0:
                free_count += 1
                position_to_play = pos
            elif position == 1:
                user_count += 1
            if user_count == 0 and positions_checked == 3:
                return position_to_play
                
    for way in win_ways:
        for pos in way:
            x = pos//3
            y = pos % 3
            position = board[x][y]
            if position == 0:
                return position

def get_cell(squares, cell):
    '''Returns data of the cell:
            cell number, row, column, x_position, y_position
    '''
    for square in squares:
        if square[5] == cell:
            sq = {
                'cell' : cell, 
                'row' : cell//3,
                'column' : cell%3,
                'x_position' : square[1]+100,
                'y_position' : square[3]+100,   
            }
            return sq

def get_machine_position(board):
    '''Checks win and block position, if not of them available
       chooses a random one (being able to win)
    '''
    to_win = get_position_to_win(board)
    if to_win:
        return to_win
    
    to_block = get_position_to_block(board)
    if to_block:
        return to_block
    
    else:
        return get_position_to_play(board)