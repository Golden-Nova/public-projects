#requirements implements a class called Game that represents a Game in python memory.
#designed to be be quickly extracted to a database

RED = 1
YELLOW = 0

class Game:
    def __init__(self, red_player : str = None, yellow_player : str = None, red_username : str = None,
    yellow_username : str = None, board : list = [[None for x in range(7)] for x in range(6)], turn : int = RED, winner = None):
        """Creates a new mutable game object. Has many, many optional arguments. Designed to be created out of 
        a database query, changed and re stored"""
        self.red_player = red_player
        self.yellow_player = yellow_player
        self.red_username = red_username
        self.yellow_username = yellow_username
        self.board = board
        self.turn = turn
        self.winner = winner

    def add_red(self, red_player_id, red_player_name) -> bool:
        """if the red player hasn't been added, adds the red player. return true if successful"""
        if self.red_player is None and self.red_username is None:
            self.red_player, self.red_username = red_player_id, red_player_name
            return True
        else:
            return False
        
    def add_yellow(self, yellow_player_id, yellow_player_name) -> bool:
        """if the yellow player hasn't been added, adds the red player. return true if successful"""
        if self.red_player is None and self.red_username is None:
            self.red_player, self.red_username = yellow_player_id, yellow_player_id
            return True
        else:
            return False
    
    def valid_move(self, column : int) -> bool:
        """checks if a move is valid"""
        return self.board[column][-1] is None
        
    def make_move(self, player_color : int, column : int) -> bool:
        """assuming it is the correct player's turn, attempts to make a move. if successful returns True and False otherwise"""
        if self.valid_move(column):
            for i in range(7):
                if self.board[column][i] is not None:
                    continue
                else:
                    self.board[column][i] = player_color
                    return True
        return False

    def game_status(self):
        """return the current status of the Game"""
        if self.yellow_player is None or self.red_player is None:
            return "Not Started"
        elif self.update_winner() is not None:
            return f"Game Over"
        else:
            return "In Progress"
        
    def update_winner(self) -> bool:
        """updates the winner attribute, returns True if the Game is Over"""
        win_list = ['YELLOW', 'RED']
        full = True
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell is None:
                    full = False
                    continue
                else:
                    if x > 2:
                        if cell == self.board[y][x - 1] == self.board[y][x - 2] == self.board[y][x - 3]:
                            self.winner = win_list[cell]
                            return True
                    if y > 2:
                        if cell == self.board[y - 1][x] == self.board[y - 2][x] == self.board[y - 3][x]:
                            self.winner = win_list[cell]
                            return True
                    if x > 2 and y > 2:
                        if cell == self.board[y - 1][x - 1] == self.board[y - 2][x - 2] == self.board[y - 3][x - 3]:
                            self.winner = win_list[cell]
                            return True
                    if x < 4 and y > 2:
                        if cell == self.board[y - 1][x + 1] == self.board[y - 2][x + 2] == self.board[y - 3][x + 3]:
                            self.winner = win_list[cell]
                            return True
        if full:
            self.winner = 'Tie'
            return True