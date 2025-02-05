from typing import Union

import requests

from utils.api_utils import ApiUtils


class MovieHelper:
    MOVIES_ENDPOINT = "/movies"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_movie(self, json) -> requests.Response:
        response = self.api_utils.post(self.MOVIES_ENDPOINT, json=json)
        return response

    # мое

    def get_movie(self, json, id: Union[int]) -> requests.Response:
        response = self.api_utils.get(self.MOVIES_ENDPOINT + '/' + str(id), json=json)
        return response
