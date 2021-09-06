# importing the module
import imdb_results

# creating instance of IMDb
ia = imdb_results.IMDb()

# movie name
name = "Tarzan the wonder car"

# searchning the movie
search = ia.search_movie(name)

# printing the result
print(search)

# importing the module
import imdb_results

# creating instance of IMDb
ia = imdb_results.IMDb()

# getting the movie info set of data base
info = ia.get_movie_infoset()

# printing the list
for element in info:
   print(element)

# importing the module
import imdb_results

# creating instance of IMDb
ia = imdb_results.IMDb()

# ID
code = "1187043"

# getting movie
movie = ia.get_movie(code)

# printing movie object
print(movie)

print("===============")

# getting cast
cast = movie['cast']

# actor name from caste
actor = cast[0]

# printing actor name
print(actor)

# importing the module
import imdb_results

# creating instance of IMDb
ia = imdb_results.IMDb()

# name
name = "Udta punjab"

# searching the name
search = ia.search_movie(name)

# loop for printing the name and id
for i in range(len(search)):
    # getting the id
    id = search[i].movieID

    # printing it
    print(search[i]['title'] + " : " + id)