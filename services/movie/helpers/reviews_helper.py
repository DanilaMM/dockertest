from typing import Union

import requests

from utils.api_utils import ApiUtils


class ReviewsHelper:
    REVIEWS_ENDPOINT = "/movies"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_reviews(self, json, id) -> requests.Response:
        response = self.api_utils.post(f"{self.REVIEWS_ENDPOINT + id}", json=json)
        return response

    def get_reviews(self, json, id: Union[int]) -> requests.Response:
        response = self.api_utils.get(self.REVIEWS_ENDPOINT + '/' + str(id), json=json)
        return response
