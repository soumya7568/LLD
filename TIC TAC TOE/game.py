from collections import deque
from requirements.player import Player
from requirements.playing_piece_Y import PlayingPieceY
from requirements.playing_piece_X import PlayingPieceX
from requirements.board import Board

class TicTacToe:
    def __init__(self) -> None:
        self.players = deque()
        self.initialize_game()
    
    def initialize_game(self):
        for i in range(2):
            choose_piece = input(f"CHoose piece for player{i}: ")
            if choose_piece=="X":
                piece_type = PlayingPieceX()
            else:
                piece_type = PlayingPieceY()
            new_player = Player(f"player{i}",piece_type)
            self.players.append(new_player)
            
        self.game_board = Board(3)
        
        
    def start_game(self):
        no_winnwer = True
        
        while no_winnwer:
            player = self.players.popleft()
            
            self.game_board.print_board()
            
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winnwer = False
                break
            
            i,j = map(int,input("Please Enter row col by a single space: ").split())
            if self.game_board.board[i][j]!=0:
                print("Incorect position choosen. Choose again")
                continue
            self.game_board.add_piece(i,j,player.playing_piece)
            self.players.append(player)
            
            winnwer = self.is_winner_found(i,j,player.playing_piece)
            if winnwer:
                return player.get_name()
        
        return "Tie"
            
            
    def is_winner_found(self,row,col,playing_piece):
        row_match = col_match = digonal_match = anti_digonal_match = True
        
        for i in range(self.game_board.size):
            if self.game_board.board[row][i]==0 or self.game_board.board[row][i].piece_type!=playing_piece.piece_type:
                row_match = False
                break
            
        for i in range(self.game_board.size):
            if self.game_board.board[i][col]==0 or self.game_board.board[i][col].piece_type!=playing_piece.piece_type:
                col_match = False
                break
            
        for i in range(self.game_board.size):
            if self.game_board.board[i][i]==0 or self.game_board.board[i][i].piece_type!=playing_piece.piece_type:
                digonal_match = False
                break
            
        for i in range(self.game_board.size-1,-1,-1):
            if self.game_board.board[self.game_board.size-i][i]==0 or self.game_board.board[self.game_board.size-i][i].piece_type!=playing_piece.piece_type:
                anti_digonal_match = False
                break
        return row_match or col_match or digonal_match or anti_digonal_match
            
        