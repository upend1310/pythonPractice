fav_movies = ['Sandlot', 'Terminator', 'Matrix']
print(fav_movies.sort())
print(len(fav_movies))
print(fav_movies[1:])
print(fav_movies[1:2])
lucky_numbers = [1, 2, 3, 4, 5, 6]
fav_movies.extend(lucky_numbers)
print(fav_movies)
fav_movies.append(9)
print(fav_movies)
fav_movies.insert(1, 'Kelly')
print(fav_movies)
fav_movies.remove("Sandlot")
print(fav_movies)
print(fav_movies.index("Terminator"))
print(fav_movies.count("Terminator"))

print(fav_movies.reverse())
fav_movies2 = fav_movies.copy()
print(fav_movies2)
fav_movies.pop()
print(fav_movies)
fav_movies.clear()
print(fav_movies)

# print(fav_movies.index("Sandlot"))

