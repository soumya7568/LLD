
class Board:
    
    def __init__(self,size:int) -> None:
        self.size = size
        self.board = [[0]*size for i in range(size)]
        
    
    def add_piece(self,row,col,piece):
        if self.board[row][col]!=0:
            return False
        self.board[row][col] = piece
        return True
    
    def get_free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]==0:
                    free_cells.append((i,j))
        return free_cells
    
    def print_board(self):
        for row in self.board:
            curr = " | ".join([cell.piece_type.value if cell else " " for cell in row])
            print(curr)
            print("-" * (self.size * 4 - 1))
                    