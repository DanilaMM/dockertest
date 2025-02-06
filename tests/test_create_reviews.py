import pytest

from logger.logger import Logger
import requests
from faker import Faker
import random
from services.movie.models.reviews.create_reviews import CreateReviews
from services.movie.models.reviews.create_reviews_response import ReviewsResponse

faker = Faker()


class TestReviewsCreate:

    @pytest.mark.sssss
    def test_revirews_create(self, movie_service_super_admin):
        pass
        # Logger.info('### Steps1. Создание отзыва к фильму')
        # text = faker.text(max_nb_chars=100)
        # reviews = CreateReviews(raiting=random.randint(1, 5),
        #                         text=text)
        # create_reviews = movie_service_super_admin.post_reviews(reviews, 3)
        #
        # assert create_reviews.text == text
