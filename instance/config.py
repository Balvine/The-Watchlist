MOVIE_API_KEY = '2a7aa1337248c047b356927474f962b0'
SECRET_KEY = 'barl'
import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

