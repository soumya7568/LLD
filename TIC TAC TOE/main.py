from game import TicTacToe
from requirements.playing_piece_X import PlayingPieceX

def main():
    game = TicTacToe()
    winner = game.start_game()
    if winner=="Tie":
        print("game is Tie")
    else:
        print(f"Winner is {winner}")
        
main()