#!/Users/BadWizard/anaconda3/envs/py36/bin/python
from movie import Movie


class User:

    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, name, genre):
        new_movie = Movie(name, genre, watched=False)
        self.movies.append(new_movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    def __repr__(self):

        return "<User {}>".format(self.name, end='')

    def watched_movies(self):
        "Collect a list of movies that were watched"

        return list(filter(lambda movie: movie.watched, self.movies))

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    @classmethod
    def from_json(cls, json_data):
        username = json_data['name']
        movies = json_data['movies']

        user = cls(username)
        for movie_data in movies:
            user.movies.append(Movie.from_json(movie_data))
        return user

    # def save_to_file(self):
#
        # with open(self.name + '.txt', 'w') as f:
        #f.write(self.name + '\n')
        # for movie in self.movies:
        #f.write('{}, {}, {}\n'.format(movie.name, movie.genre, str(movie.watched)))
#
    #@classmethod
    # def load_from_file(cls, filename):
        # with open(filename, 'r') as f:
        #content = f.readlines()
        # username = content[0].strip()  # gets rid of the end-of-line
        #movies = []
        # for line in content[1:]:
        #name, genre, watched = line.replace(' ', '').split(',')
        #movies.append(Movie(name, genre, watched == 'True'))
#
        #user = cls(username)
        #user.movies = movies
#
        # return user
