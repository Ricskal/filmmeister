from IMDBapi import IMDB

prod = 1
imdb_code = "tt0450385"

test = IMDB.get_movie(prod, imdb_code)
print(test)