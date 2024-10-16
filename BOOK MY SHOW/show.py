from movie import Movie
from screen import Screen

class Show:
    def __init__(self,show_id,movie : Movie,screen: Screen,start_time,booked_seats=[]) -> None:
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.booked_seats = booked_seats
        
    @property
    def show_id(self):
        return self._show_id

    @show_id.setter
    def show_id(self, value):
        self._show_id = value

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, value):
        self._movie = value

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def booked_seats(self):
        return self._booked_seats

    @booked_seats.setter
    def booked_seats(self, value):
        self._booked_seats = value