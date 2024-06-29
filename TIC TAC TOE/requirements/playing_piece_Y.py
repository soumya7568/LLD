from requirements.playing_piece import PlayingPiece
from requirements.piece_type import PieceType

class PlayingPieceY(PlayingPiece):
    
    def __init__(self):
        super().__init__(PieceType.PIECE_Y)