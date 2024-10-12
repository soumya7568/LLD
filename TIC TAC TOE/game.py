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
        has = {"X":False,"Y":False}
        flag = False
        while not flag:
            choose_piece = input(f"Choose piece for player{1}: from X or Y: ")
            if choose_piece not in ["X","Y"]:
                print("Wrong choice. Choose again")
                continue
            flag = True
            
        if choose_piece=="X":
            piece_type = PlayingPieceX()
        else:
            piece_type = PlayingPieceY()
        new_player = Player(f"player{1}",piece_type)
        self.players.append(new_player)
        has[choose_piece] = True
        
        if not has["Y"]:
            piece_type = PlayingPieceY()
        else:
            piece_type = PlayingPieceX()
        new_player = Player("player2",piece_type)
        self.players.append(new_player)
        self.game_board = Board(3)
        
        
    def is_valid_move(self,i,j):
        if 0<=i<3 and 0<=j<=3:
            return True
        return False
        
    def start_game(self):
        no_winnwer = True
        
        while no_winnwer:
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winnwer = False
                break
            i,j = map(int,input("Please Enter row col by a single space: ").split())
            
            if not self.is_valid_move(i,j):
                print("Incorect position choosen. Choose again")
                continue
            
            player = self.players.popleft()
            
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
        
        # row match
        for i in range(self.game_board.size):
            if self.game_board.board[row][i]==0 or self.game_board.board[row][i].piece_type!=playing_piece.piece_type:
                row_match = False
                break
            
        # col match
        for i in range(self.game_board.size):
            if self.game_board.board[i][col]==0 or self.game_board.board[i][col].piece_type!=playing_piece.piece_type:
                col_match = False
                break
            
        # digonal match
        for i in range(self.game_board.size):
            if self.game_board.board[i][i]==0 or self.game_board.board[i][i].piece_type!=playing_piece.piece_type:
                digonal_match = False
                break
            
        # anti digonal match
        for i in range(self.game_board.size-1,-1,-1):
            if self.game_board.board[self.game_board.size-i][i]==0 or self.game_board.board[self.game_board.size-i][i].piece_type!=playing_piece.piece_type:
                anti_digonal_match = False
                break
        return row_match or col_match or digonal_match or anti_digonal_match
            
        