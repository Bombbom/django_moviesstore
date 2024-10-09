from movies.models import Movie 

movies = Movie.objects.all()

for movie in movies:
    print(movie.image.url)