from movie import Movie
from collections import defaultdict

class MovieController:
    
    def __init__(self) -> None:
        self.city_movie_map = defaultdict(list)
        self.movies = []
        
    def add_movies(self,movie,city):
        self.movies.append(movie)
        self.city_movie_map[city].append(movie)
        
    def get_movie_by_name(self,movie_name):
        for movie in self.movies:
            if movie.movie_name == movie_name:
                return movie
        return None
    
    def get_movies_by_city(self,city):
        return self.city_movie_map[city]