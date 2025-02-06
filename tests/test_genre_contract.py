import pytest
import requests
from faker import Faker

from services.movie.helpers.genre_helper import GenreHelper

faker = Faker()


class TestGenreContract:
    @pytest.mark.xxx
    def test_genre_contrat_anonym(self, api_utils_anonym_auth):
        pass
        # genre_helper = GenreHelper(api_utils=api_utils_anonym_auth)
        # response = genre_helper.post_genre({"name": faker.name})
        #
        # assert response.status_code == 401
