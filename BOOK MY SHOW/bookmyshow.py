from movie_controller import MovieController
from theatre_controller import TheatreController
from movie import Movie
from theatre import Theatre
from location import Location
from screen import Screen
from seat import Seat
from enums import SeatType
import math
from show import Show
from booking import Booking

class BookMyShow:
    
    def __init__(self) -> None:
        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()
        self.initialize()
        
    def initialize(self):
        self.create_movies()
        self.create_theatres()
    
    def create_movies(self):
        avengers = Movie()
        avengers.movie_id = 1
        avengers.movie_name = "AVENGERS"
        avengers.movie_language = "English"
        avengers.movie_genre = "Action"
        avengers.movie_duration = 185
        
        abcd = Movie()
        abcd.movie_id = 1
        abcd.movie_name = "ABCD"
        abcd.movie_language = "Hindi"
        abcd.movie_genre = "comedy"
        abcd.movie_duration = 136
        
        self.movie_controller.add_movies(avengers,"Delhi")
        self.movie_controller.add_movies(avengers,"Hyderabad")
        self.movie_controller.add_movies(abcd,"Hyderabad")
        self.movie_controller.add_movies(abcd,"Delhi")
        
        
    
    def create_theatres(self):
        avengers = self.movie_controller.get_movie_by_name("AVENGERS")
        abcd = self.movie_controller.get_movie_by_name("ABCD")
        
        delhi = Location("754202","Delhi","Delhi","India")
        hyderabad = Location("716232","Hyderabad","Telengana","India")
        
        inox = Theatre(1,delhi)
        inox.screens = self.create_sceen()
        morning_inox = self.create_shows(1,inox.screens[0],avengers,8)
        evening_inox = self.create_shows(2,inox.screens[0],abcd,16)
        inox.shows = [morning_inox,evening_inox]
        
        pvr = Theatre(2,hyderabad)
        pvr.screens = self.create_sceen()
        morning_pvr = self.create_shows(3,pvr.screens[0],avengers,9)
        evening_pvr = self.create_shows(4,pvr.screens[0],abcd,14)
        inox.shows = [morning_pvr,evening_pvr]
        
        self.theatre_controller.add_theatres(inox,delhi.city)
        self.theatre_controller.add_theatres(pvr,hyderabad.city)
        
        
    def create_sceen(self):
        screens = []
        screen1 = Screen()
        screen1.screen_id = 1
        screen1.seats = self.create_seats()
        screens.append(screen1)
        return screens
        
    def create_seats(self):
        seats = []
        for i in range(1,41):
            seat = Seat(i,SeatType.SILVER,math.ceil(i/10))
            seats.append(seat)
            
        for i in range(41,71):
            seat = Seat(i,SeatType.GOLD,math.ceil(i/10))
            seats.append(seat)      
        
        for i in range(71,101):
            seat = Seat(i,SeatType.PLAINUM,math.ceil(i/10))
            seats.append(seat)  

        return seats
    
    def create_shows(self,show_id,screen,movie,start_time):
        return Show(show_id,movie,screen,start_time)
        
    def create_booking(self,city,movie_name):
        try:
            movies = self.movie_controller.get_movies_by_city(city)
            intersted_movie = None
            for movie in movies:
                if movie.movie_name==movie_name:
                    intersted_movie = movie
                    
            shows_theatre_wise = self.theatre_controller.get_all_shows(intersted_movie,city)
            for key,value in shows_theatre_wise.items():
                intersted_show = value[0]
                
            booked_seats = intersted_show.booked_seats
            intersted_seat = 23
            if intersted_show not in booked_seats:
                booked_seats.append(intersted_seat)
                
                booking = Booking()
                my_booked_seats = []
                screen_seats = intersted_show.screen.seats
                for screen_seat in screen_seats:
                    if screen_seat.seat_id==intersted_seat:
                        my_booked_seats.append(screen_seat)
                booking.booked_seats = my_booked_seats
                booking.show = intersted_show
            else:
                print("Choosed seat is not available")
                return
            print("Seat booked successfully")
                
                    
        except Exception as e:
            print(e)
            return