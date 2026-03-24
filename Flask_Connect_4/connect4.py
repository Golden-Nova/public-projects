#requirements
# has a Game dataclass that acts as an immutable version of a game
from dataclasses import dataclass

@dataclass(frozen=True)
class Game:
    red_player : str = None
    yellow_player : str = None
    red_username : str = None
    yellow_username : str = None
    board : tuple = ((None for x in range(7)) for x in range(6))
    turn : int = 1

    def add_red(self, red_player_id, red_player_name):
        """if a red player hasn't joined the game yet, returns the same game with him joined.
        if a red player has joined the game, return None"""
        if self.red_player is None and self.red_username is None:
            return Game(red_player = red_player_id, yellow_player= self.yellow_player, red_username=red_player_name, \
                    yellow_username= self.yellow_username, board= self.board, turn= self.turn)
        else:
            return None
        
    def add_red(self, yellow_player_id, yellow_player_name):
        """if a red player hasn't joined the game yet, returns the same game with him joined.
        if a red player has joined the game, return None"""
        if self.yellow_player is None and self.yellow_username is None:
            return Game(red_player = self.red_player, yellow_player= yellow_player_id, red_username=self.red_username, \
                    yellow_username= yellow_player_name, board= self.board, turn= self.turn)
        else:
            return None
