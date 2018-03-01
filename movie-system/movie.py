#!/Users/BadWizard/anaconda3/envs/py36/bin/python
class Movie:

    def __init__(self, name, genre, watched=False):
        self.name = name
        self.genre = genre
        self.watched = watched

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        # return cls(json_data['name'], json_data['genre'], json_data['watched'])
        return cls(**json_data)

    def __repr__(self):

        return "<{}>".format(self.name)
