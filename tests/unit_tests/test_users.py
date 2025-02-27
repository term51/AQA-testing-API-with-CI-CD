import allure
import pytest

from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        # ... и все остальные проверки

        print("check created user:", self.api_users.get_user_by_id(user.uuid))
