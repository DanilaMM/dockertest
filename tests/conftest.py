import os

import pytest

from services.movie.movie_service import MovieService
from services.auth.auth_service import AuthService
from services.auth.models.authorization.login_user_dto import LoginUserDto
from utils.api_utils import ApiUtils

AUTH_API_URL = "https://auth.dev-cinescope.store"
MOVIE_API_URL = "https://api.dev-cinescope.store"


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_auth():
    api_utils_anonym = ApiUtils(url=AUTH_API_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_api():
    api_utils_anonym = ApiUtils(url=MOVIE_API_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_super_admin_movie(api_utils_anonym_auth):
    email = "mailsuu@mail.ru"#os.environ["SUPER_ADMIN_EMAIL"]
    password = "dddooolll1112"#os.environ["SUPER_ADMIN_PASSWORD"]

    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    login_user = LoginUserDto(email=email, password=password)
    #login_response = auth_service.login_user(login_user)

    #api_utils_super_admin = ApiUtils(url=MOVIE_API_URL,
    #                                headers={'Authorization': f"Bearer {login_response.access_token}"})

    #yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def movie_service_super_admin(api_utils_super_admin_movie):
    movie_service = MovieService(api_utils=api_utils_super_admin_movie)
    yield movie_service
