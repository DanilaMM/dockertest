from services.movie.helpers.genre_helper import GenreHelper
from services.movie.helpers.movie_helper import MovieHelper
from services.movie.helpers.reviews_helper import ReviewsHelper
from services.movie.models.genre.create_genre_dto import CreateGenreDto
from services.movie.models.genre.genre_response import GenreResponse
from services.movie.models.movie.create_movie_dto import CreateMovieDto
from services.movie.models.movie.movie_response import MovieResponse
from services.movie.models.reviews.create_reviews import CreateReviews
from services.movie.models.reviews.create_reviews_response import ReviewsResponse


class MovieService:
    def __init__(self, api_utils):
        self.api_utils = api_utils

        self.genre_helper = GenreHelper(self.api_utils)
        self.movie_helper = MovieHelper(self.api_utils)
        self.reviews_helper = ReviewsHelper(self.api_utils)

    def post_genre(self, create_genre: CreateGenreDto):
        response = self.genre_helper.post_genre(json=create_genre.model_dump(by_alias=True,
                                                                             exclude_defaults=True))
        return GenreResponse(**response.json())

    def post_movie(self, create_movie: CreateMovieDto):
        response = self.movie_helper.post_movie(create_movie.model_dump(by_alias=True,
                                                                        exclude_defaults=True))
        return MovieResponse(**response.json())

    def post_genre_and_movie(self):
        raise NotImplementedError

    def post_random_genre(self):
        pass

    def post_reviews(self, create_reviews: CreateReviews, id):
        response = self.reviews_helper.post_reviews(create_reviews.model_dump(by_alias=True,
                                                                              exclude_defaults=True), id)
        return ReviewsResponse(**response.json())
