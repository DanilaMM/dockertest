import random
from services.auth.helpers.authorization_helper import AuthorizationHelper
from faker import Faker
import os

from services.movie.helpers.genre_helper import GenreHelper
from services.movie.helpers.movie_helper import MovieHelper
from utils.api_utils import ApiUtils

faker = Faker()

AUTH_API_URL = "https://auth.dev-cinescope.store"
MOVIE_API_URL = "https://api.dev-cinescope.store"

email = os.environ["SUPER_ADMIN_EMAIL"]
password = os.environ["SUPER_ADMIN_PASSWORD"]

public_auth_api_utils = ApiUtils(url=AUTH_API_URL)
authorization_helper = AuthorizationHelper(public_auth_api_utils)
response = authorization_helper.post_login(
    json={
        "email": email,
        "password": password,
    }
)

access_token = response.json()["accessToken"]

super_admin_movie_api_utils = ApiUtils(url=MOVIE_API_URL, headers={'Authorization': f"Bearer {access_token}"})
genre_helper = GenreHelper(super_admin_movie_api_utils)
movie_helper = MovieHelper(super_admin_movie_api_utils)

response = genre_helper.post_genre(
    json={"name": faker.name()},
)
genre_id = response.json()["id"]

response = movie_helper.post_movie(
    json={"name": faker.name(),
          "imageUrl": faker.url(),
          "price": random.randint(10, 100),
          "description": faker.text(),
          "location": random.choice(["SPB", "MSK"]),
          "published": True,
          "genreId": genre_id}, )

print(response.json())
