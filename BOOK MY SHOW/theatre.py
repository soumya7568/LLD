from location import Location
from screen import Screen
from show import Show

class Theatre:
    def __init__(self, theatre_id, theatre_location : Location):
        self.theatre_id = theatre_id
        self.theatre_location = theatre_location
        self._screens = []
        self._shows = []
        
    @property
    def screens(self):
        return self._screens

    @screens.setter
    def screens(self, value):
        self._screens = value
        
    @property
    def shows(self):
        return self._shows

    @screens.setter
    def shows(self, value):
        self._shows = value
        
        