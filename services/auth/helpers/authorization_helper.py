import requests

from utils.api_utils import ApiUtils


class AuthorizationHelper:
    REGISTER_ENDPOINT = "/register"
    LOGIN_ENDPOINT = "/login"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_register(self, json) -> requests.Response:
        response = self.api_utils.post(self.REGISTER_ENDPOINT, json=json)
        return response

    def post_login(self, json) -> requests.Response:
        response = self.api_utils.post(self.LOGIN_ENDPOINT, json=json)
        return response
