from logger.logger import Logger
import requests
from faker import Faker
import random
from services.movie.models.genre.create_genre_dto import CreateGenreDto
from services.movie.models.movie.create_movie_dto import CreateMovieDto, LocationEnum

faker = Faker()


class TestMovieCreate:
    def test_movie_create(self, movie_service_super_admin):
        pass
        # Logger.info('### Steps1. Create genre')
        # genre = CreateGenreDto(name=faker.name())
        # create_genre = movie_service_super_admin.post_genre(genre)
        # movie = CreateMovieDto(
        #     name=faker.name(),
        #     price=random.randint(1, 1000),
        #     description=faker.pystr(),
        #     location=LocationEnum.SPB,
        #     published=True,
        #     genre_id=create_genre.id,
        #     image_url="https://google.com/",
        # )
        # Logger.info('Steps 2 . Cteate movies')
        # created_movie = movie_service_super_admin.post_movie(movie)
        # assert created_movie.genre.name == genre.name
