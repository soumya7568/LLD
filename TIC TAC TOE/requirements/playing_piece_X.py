from requirements.playing_piece import PlayingPiece
from requirements.piece_type import PieceType

class PlayingPieceX(PlayingPiece):
    
    def __init__(self):
        super().__init__(PieceType.PIECE_X)