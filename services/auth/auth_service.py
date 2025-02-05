from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.auth.models.authorization.login_user_dto import LoginUserDto
from services.auth.models.authorization.login_response import LoginResponse
from utils.api_utils import ApiUtils


class AuthService:
    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.authorization_helper = AuthorizationHelper(self.api_utils)

    def register_user(self):
        raise NotImplementedError

    def login_user(self, login_user: LoginUserDto):
        response = self.authorization_helper.post_login(login_user.model_dump(by_alias=True,
                                                                              exclude_defaults=True))
        return LoginResponse(**response.json())
