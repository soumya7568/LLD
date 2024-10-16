
class Movie:
    def __init__(self,movie_id=None,movie_name=None,movie_language=None,movie_genre=None,movie_duration=None) -> None:
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_language = movie_language
        self.movie_genre = movie_genre
        self.movie_duration = movie_duration
        
    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, value):
        self._movie_id = value

    @property
    def movie_name(self):
        return self._movie_name

    @movie_name.setter
    def movie_name(self, value):
        self._movie_name = value

    @property
    def movie_language(self):
        return self._movie_language

    @movie_language.setter
    def movie_language(self, value):
        self._movie_language = value

    @property
    def movie_genre(self):
        return self._movie_genre

    @movie_genre.setter
    def movie_genre(self, value):
        self._movie_genre = value

    @property
    def movie_duration(self):
        return self._movie_duration

    @movie_duration.setter
    def movie_duration(self, value):
        self._movie_duration = value
        
        
movie = Movie()

# movie.movie_id = 23
movie.movie_id(23)
print(movie.movie_id)