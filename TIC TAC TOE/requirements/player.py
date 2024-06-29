class Player:
    
    def __init__(self,name,playing_piece) -> None:
        self._name = name
        self.playing_piece = playing_piece
        
    def get_name(self):
        return self._name
    
    def get_playing_piece(self):
        return self.playing_piece