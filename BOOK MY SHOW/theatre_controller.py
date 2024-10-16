from collections import defaultdict

class TheatreController:
    
    def __init__(self) -> None:
        self.city_theatre_map = defaultdict(list)
        self.theatres = []
        
    def add_theatres(self,theatre,city):
        self.theatres.append(theatre)
        self.city_theatre_map[city].append(theatre)
        
    def get_all_shows(self,movie,city):
        theatres = self.city_theatre_map.get(city)
        
        threatres_movie_map = defaultdict(list)
        
        for theatre in theatres:
            movie_shows = []
            all_shows = theatre.shows
            for show in all_shows:
                if show.movie.movie_id==movie.movie_id:
                    movie_shows.add(show)
                    
            if movie_shows:
                threatres_movie_map[theatre] = movie_shows
        return threatres_movie_map