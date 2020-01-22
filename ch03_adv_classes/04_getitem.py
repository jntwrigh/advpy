class TopMovies:
    def __init__(self, movies=None):
        if movies is None:
            self.movies = [
                ('Avatar', 2787965087, 2009),
                ('Titanic', 2186772302, 1997),
                ('Jurassic World', 1651382496, 2015),
                ('The Avengers', 1519557910, 2012),
                ('Furious 7', 1511726205, 2015)
            ]

    def __len__(self):
        return len(self.movies)

    def __getitem__(self, key):
        return self.movies[key]

    def __setitem__(self, key, value):
        self.movies[key] = value

    def __delitem__(self, key):
        del self.movies[key]

    def __iter__(self):
        return iter(self.movies)


tm = TopMovies()
del tm[3]
for movie in tm:
    print(movie)

print(tm[0])
print(tm[-2:])
