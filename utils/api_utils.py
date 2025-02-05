import json

import requests
from requests import Session
from logger.logger import Logger
import curlify

from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)
        Logger.info(f"Request {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code = {response.status_code}, elapsed_time = {response.elapsed}, {body}")
        return response

    return _log_response


class ApiUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}

        self.session = Session()
        self.session.headers.update(headers)
        self.url = url

    def update_headers(self, headers):
        self.session.headers.update(headers)

    @log_response
    def get(self, endpiont_url, **kwargs) -> requests.Response:
        response = self.session.get(self.url + endpiont_url, **kwargs)
        return response

    @log_response
    def post(self, endpoint_url, data=None, json=None, **kwargs):
        response = self.session.post(self.url + endpoint_url, data, json, **kwargs)
        return response
