#requirements
# has a Game dataclass that acts as an immutable version of a game
from dataclasses import dataclass

@dataclass(frozen=True)
class Game:
    red_player : str = None
    yellow_player : str = None
    red_username : str = None
    red_username : str = None
    board : tuple = ((None for x in range(7)) for x in range(6))
    turn : int = 1
