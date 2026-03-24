#requirements
# has a Game dataclass that acts as an immutable version of a game
from dataclasses import dataclass

RED = 1
YELLOW = 0


@dataclass(frozen=True)
class Game:
    red_player : str = None
    yellow_player : str = None
    red_username : str = None
    yellow_username : str = None
    board : tuple = ((None for x in range(7)) for x in range(6))
    turn : int = RED

    def add_red(self, red_player_id, red_player_name):
        """if a red player hasn't joined the game yet, returns the same game with him joined.
        if a red player has joined the game, return None"""
        if self.red_player is None and self.red_username is None:
            return Game(red_player = red_player_id, yellow_player= self.yellow_player, red_username=red_player_name, \
                    yellow_username= self.yellow_username, board= self.board, turn= self.turn)
        else:
            return None
        
    def add_yellow(self, yellow_player_id, yellow_player_name):
        """if a red player hasn't joined the game yet, returns the same game with him joined.
        if a red player has joined the game, return None"""
        if self.yellow_player is None and self.yellow_username is None:
            return Game(red_player = self.red_player, yellow_player= yellow_player_id, red_username=self.red_username, \
                    yellow_username= yellow_player_name, board= self.board, turn= self.turn)
        else:
            return None
    
    def game_status(self):
        """return the current status of the Game"""
        if self.yellow_player is None or self.red_player is None:
            return "Not Started"
        elif self.winner() is not None:
            return f"Finished. winner : {self.winner()}"
        else:
            return "In Progress"
        
    def winner(self) -> str:
        win_list = ['YELLOW', 'RED']
        full = True
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == None:
                    full = False
                    continue
                else:
                    if x > 2:
                        if cell == self.board[y][x - 1] == self.board[y][x - 2] == self.board[y][x - 3]:
                            return win_list[cell]
                    if y > 2:
                        if cell == self.board[y - 1][x] == self.board[y - 2][x] == self.board[y - 3][x]:
                            win_list[cell]
                    if x > 2 and y > 2:
                        if cell == self.board[y - 1][x - 1] == self.board[y - 2][x - 2] == self.board[y - 3][x - 3]:
                            win_list[cell]
                    if x < 4 and y > 2:
                        if cell == self.board[y - 1][x + 1] == self.board[y - 2][x + 2] == self.board[y - 3][x + 3]:
                            return win_list[cell]
        if full:
            return 'tie'

