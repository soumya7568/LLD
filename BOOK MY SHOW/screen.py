
class Screen:
    def __init__(self,screen_id,seats:list) -> None:
        self.screen_id = screen_id
        self.seats = seats
        
    @property
    def screen_id(self):
        return self._screen_id

    @screen_id.setter
    def screen_id(self, value):
        self._screen_id = value

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value
        
