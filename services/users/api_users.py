"""

"""
import allure
import requests

from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers

from services.users.models.user_model import UserModel

from utils.helper import Helper


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()  # расширение дочернего класса

        # подключаем классы для работы с API Users
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())  # при создании объекта UserModel будут валидироваться все поля
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),  # get_user_by_id Lambda функция
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())  # при создании объекта UserModel будут валидироваться все поля
        return model
