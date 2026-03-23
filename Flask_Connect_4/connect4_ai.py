#Requirements:
#if given a connect4 board and a color generates a move at the given difficulty level
# easy move:
#   takes winning move -> stops opponent winning move -> generates random legal move
# medium move:
#   "looks 5 moves into the future" rating moves like stockfish -> chooses random highest rated move
# hard move:
#      "looks 15 moves into the future" rating moves like stockfish -> chooses random highest rated move
# impossible move:
#   uses libary of solved connect 4 to choose perfect move. actually impossible if moves first
